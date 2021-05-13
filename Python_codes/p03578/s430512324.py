n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

from collections import Counter

dc = Counter(d)
dt = Counter(t)

for k, v in dt.items():
	if dc[k] < v:
		print('NO')
		exit()

print('YES')