# n, k = map(int, input().split())
# n = int(input())
# li = list(map(int, input().split()))
s = input()
from collections import Counter
d = Counter(s)
if len(d.keys()) == 2 and all(i == 2 for i in d.values()):
	print("Yes")
else:
	print("No")