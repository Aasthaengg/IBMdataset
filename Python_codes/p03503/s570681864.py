from itertools import product

bit = [0, 1]

lst = list(product(bit, repeat=10))

n = int(input())
F = [list(map(int, input().split())) for i in range(n)]
P = [list(map(int, input().split())) for j in range(n)]

res = -1 << 30
for v in lst:
	if v.count(0) == 10: continue
	fund = 0
	for i in range(n):
		cnt = 0
		for x in range(10):
			if F[i][x] == 1 and v[x] == 1:
				cnt += 1
		fund += P[i][cnt]
	res = max(res, fund)

print(res)