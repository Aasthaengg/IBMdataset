from scipy.special import comb
N, M = map(int, input().split())
ans = 0
if N >= 2:
    ans += comb(N, 2, exact=True)
if M >= 2:
    ans += comb(M, 2, exact=True)
print(ans)