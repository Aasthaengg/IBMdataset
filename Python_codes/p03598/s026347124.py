n = int(input())
k = int(input())

X = tuple(map(int, input().split()))

ans = 0
for i in range(n):
    ans += min(2*X[i], 2*abs(X[i] - k))
print(ans)