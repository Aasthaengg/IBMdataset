n, a, b = map(int,input().split())
nmax = min(a, b)
nmin = max(a + b - n, 0)
print(nmax, nmin, sep = " ")