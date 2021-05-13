N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 10**9
for i in range(N-K+1):
    l, r = A[i], A[i+K-1]
    if l*r >= 0:
        ans = min(ans, max(abs(l), abs(r)))
    else:
        ans = min(ans, r-l+min(abs(l), abs(r)))
print(ans)
