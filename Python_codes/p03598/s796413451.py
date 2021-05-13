N = int(input())
K = int(input())
X = [int(a) for a in input().split()]

ans = 0
for i in range(N):
    a = X[i] * 2
    b = abs(X[i]-K) * 2
    ans += min(a, b)
print(ans)