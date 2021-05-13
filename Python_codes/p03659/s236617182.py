N, *A = map(int, open(0).read().split())

S = sum(A)
k = 0
ans = 10**18
for i,a in enumerate(A, start=1):
    k += a
    if N == i:
        break
    ans = min(ans, abs(S - 2*k))
print(ans)
