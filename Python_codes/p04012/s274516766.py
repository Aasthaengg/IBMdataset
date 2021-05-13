from collections import Counter
W = input()
x = Counter(W)
for x1 in x.values():
	if x1 % 2 == 1:
		print('No')
		exit()
		
print('Yes')