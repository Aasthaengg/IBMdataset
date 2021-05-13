n, m, d = map(int, input().split())
sum = 0
patt = n-d
if d != 0:
    patt = 2 * patt
print(patt * (m-1) / (n * n))