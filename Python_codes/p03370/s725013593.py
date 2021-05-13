N, X = map(int, input().split())
M = sorted([int(input()) for _ in range(N)])
ans = (X - sum(M)) // min(M) + N
print(ans)
