N = int(input())
D,X = map(int, input().split())

A = [int(input()) for i in range(N)]

ans = 0

for i in A:
	j = 0
	while True:
		if (i*j+1) > D:
			break
		ans += 1
		j += 1

print(ans+X)

