import sys

M = 10 ** 9 + 7
N, K = map(int, input().split())

p_list = []
n_list = []
z_count = 0

for A in map(int, input().split()):
	if A < 0:
		n_list.append(A)
	elif A > 0:
		p_list.append(A)
	else:
		z_count += 1

p_list.sort()
n_list.sort()

#print(p_list)
#print(n_list)

if len(p_list) + len(n_list) < K:
	print(0)
else:
	values = []
	
	if len(p_list) + len(n_list) == K:
		values = p_list + n_list
		n_count = 0
		for v in values:
			if v < 0:
				n_count += 1
		if n_count % 2 == 1 and z_count > 0:
			values = [0]
	elif len(p_list) == 0 and K % 2 == 1:
		if z_count > 0:
			values = [0]
		else:
			for i in range(min(len(n_list), K)):
				values.append(n_list.pop())
	else:
		n_list.reverse()
		values_pair = []
		values_left = None
		values_left_count = 0
		if len(p_list) >= K:
			if K % 2 == 1:
				values_left = p_list.pop()
				values_left_count = 1
				p_count = K - 1
			else:
				p_count = K
			
			while len(values_pair) * 2 + values_left_count < K:
				v1 = p_list.pop()
				v2 = p_list.pop()
				values_pair.append((v1 * v2, v1, v2))
		
		else:
			if (K - len(p_list)) % 2 == 1 and len(p_list) > 0:
				p_count = len(p_list) - 1
			else:
				p_count = len(p_list)
			
			if p_count % 2 == 1:
				values_left = p_list.pop()
				values_left_count = 1
				p_count -= 1
			
			for i in range(0, p_count - 1, 2):
				v1 = p_list.pop()
				v2 = p_list.pop()
				values_pair.append((v1 * v2, v1, v2))
			
			while len(values_pair) * 2 + values_left_count < K:
				v1 = n_list.pop()
				v2 = n_list.pop()
				values_pair.append((v1 * v2, v1, v2))
		
		values_pair.sort()
		
#		print(values_pair)
		
		i = 0
		for i in range(len(values_pair)):
			if len(n_list) < 2:
				break
			elif values_pair[i][0] < n_list[-1] * n_list[-2]:
				v1 = n_list.pop()
				v2 = n_list.pop()
				values_pair[i] = (v1 * v2, v1, v2)
			else:
				break
		if values_left != None:
			values.append(values_left)
		
		for prod, v1, v2 in values_pair:
			values.append(v1)
			values.append(v2)
	
#	print(values)
	total = 1
	for v in values:
		total = (total * v) % M
#		total = (total * v)
	print(total)
