n, T = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
Y = []
for i in range(n-1):
    Y.append(X[i+1]-X[i])

ans = 0
for y in Y:
    ans += min(T, y)
ans += T
print(ans)
