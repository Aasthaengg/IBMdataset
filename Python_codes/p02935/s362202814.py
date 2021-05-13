
N = int(input())
X = list(map(int, input().split()))

X.sort()
ans = X[0] + X[1]
for i in range(2, N):
    ans += X[i] * 2 ** (i - 1)

print(ans / 2 ** (N - 1))
