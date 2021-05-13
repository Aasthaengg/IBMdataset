import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N, P = map(int, input().split())
A = list(map(int, input().split()))
o, e = 0, 0
for i in A:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
ans = 0
for i in range(P, o+1, 2):
    ans += comb(o, i)
print(ans * 2 ** e)
