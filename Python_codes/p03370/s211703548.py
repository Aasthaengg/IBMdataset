N, X = map(int, input().split())
M = sorted([int(input()) for _ in range(N)])

if X >= sum(M):
    min_M = min(M)
    ans = (X - sum(M)) // min_M + N
else:
    current = 0
    for i, m in enumerate(M, start=1):
        current += m
        if current > X:
            ans = i
print(ans)
