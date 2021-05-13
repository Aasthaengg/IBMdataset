import collections

S = str(input())
len_S = len(S)
K = int(input())
lst = []

for i in range(len_S):
	j = 1
	while i + j <= len_S:
		if j == 6: break
		lst.append(S[i : i + j])
		j += 1
lst.sort()

if K == 1:
	print(lst[0])
else:
	ctr = 1
	for i in range(1, len(lst)):
		if lst[i] != lst[i - 1]:
			ctr += 1
		if ctr == K:
			print(lst[i])
			break