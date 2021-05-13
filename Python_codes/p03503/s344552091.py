n = int(input())
F = [[] * 10 for _ in range(n)]
P = [[] * 10 for _ in range(n)]

for i in range(n):
	F[i] = list(map(int, input().split()))

for i in range(n):
	P[i] = list(map(int, input().split()))


res = -1<<30
for item in range(1, 1 << 10):
	fund = 0
	for i in range(n):
		cnt = 0
		for x in range(10):
			if item >> x & 1 and F[i][x] == 1:
				cnt += 1
		fund += P[i][cnt]
	res = max(res, fund)

print(res)