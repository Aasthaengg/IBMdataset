n, k = map(int, input().split())

q = (n-1) // (k-1)
r = (n-1) % (k-1)

if r: print(q+1)
else: print(q)