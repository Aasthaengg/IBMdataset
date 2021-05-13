N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]

residual = X - sum(m)
Dmax = residual // min(m)
print(Dmax + N)