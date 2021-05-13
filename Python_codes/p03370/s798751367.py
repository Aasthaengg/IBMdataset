N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]
X = X - sum(M)
ans = len(M)
m = min(M)
while X >= m:
    X -= m
    ans += 1
print(ans)