N, M, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
ans, Bi, Asum, Bsum = 0, M, 0, sum(B)
for Ai in range(N + 1):
    Asum += A[Ai]
    while Asum + Bsum > K and Bi > 0:
        Bsum -= B[Bi]
        Bi -= 1
    if Asum + Bsum <= K:
        ans = max(ans, Ai + Bi)
print(ans)
