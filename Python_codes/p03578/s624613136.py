n = int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))

from collections import Counter
DC = Counter(D)
TC = Counter(T)
for k, v in TC.items():
	if v > DC[k]:
		print("NO")
		exit()
else:
	print("YES")