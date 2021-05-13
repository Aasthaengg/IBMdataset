K, T = map(int, input().split())
A = list(map(int, input().split()))

Amax = max(A)
Asum = sum(A) - Amax

ans = max(0, Amax - Asum - 1)
print(ans)