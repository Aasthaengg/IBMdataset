from math import factorial

n = int(input())
S = [input() for _ in range(n)]
d = dict()

for s in S:
    s = ''.join(sorted(s))
    if s not in d.keys():
        d[s] = 1
    else:
        d[s] += 1

d_comb = dict()
def fact(n):
    keys = d_comb.keys()
    if n not in keys:
        d_comb[n] = factorial(n)
    return d_comb[n]

def comb(n, r):
    if n < r:
        return 0
    f_n = fact(n)
    f_nr = fact(n - r)
    f_r = fact(r)
    return f_n // (f_nr * f_r)

ans = 0
for k in d.keys():
    ans += comb(d[k], 2)
print(ans)