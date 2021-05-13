from scipy.special import comb

N, M = map(int, input().split())
ans = comb(N + M, 2, exact=True) - (N * M)

print(ans)