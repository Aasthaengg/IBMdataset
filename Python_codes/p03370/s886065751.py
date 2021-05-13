N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]
ans = 0
for m in M:
    X -= m
    ans += 1
ans += X // min(M)
print(ans)
