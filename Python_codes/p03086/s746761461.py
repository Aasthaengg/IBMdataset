S = input()
l = ['A', 'C', 'G', 'T']

start = False
counts = [0]

for i, c in enumerate(S):
	if c in l:
		if start == False:
			start = True
			count = 1
		else:
			count += 1
			
		if i == len(S) - 1:
			counts.append(count)
	else:
		if start == False:
			continue
		else:
			start = False
			counts.append(count)
			count = 0

print(max(counts))