N = int(input())
X = [tuple(map(int, input().split())) for _ in range(N)]
X = reversed(X)

ans = 0
for a, b in X:
    a += ans
    if a % b == 0:
        continue
    ans += b - a % b
print(ans)

