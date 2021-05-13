N = int(input())
K = int(input())
X = list(map(int, input().split()))

sum = 0
for i in range(N):
	dist = min(X[i], abs(X[i] - K))
	sum += dist*2

print(sum)