N, A, B = map(int, input().split())
X = tuple(map(int, input().split()))

current = X[0]

ans = 0
for x in X:
    ans += min((x - current) * A, B)
    current = x

print(ans)
