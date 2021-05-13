import math
def C(n, r):
    if n < r or r < 0:
        return 0
    else:
        return (math.factorial(n) // (math.factorial(r) * math.factorial(n - r)))

N, K = map(int,input().split())
ans = []
R = N - K
for i in range(1, K + 1):
    b = C(K - 1, i - 1)
    r = C(R - 1, i - 2) + 2 * C(R - 1, i - 1) + C(R - 1, i)
    ans.append((b * r) % (10**9 + 7))
if R == 0:
    ans = [1] + [0 for i in range(K - 1)]
print('\n'.join(list(map(str,ans))))