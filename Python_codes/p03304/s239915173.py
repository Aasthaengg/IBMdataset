def inpl(): return list(map(int, input().split()))
n, m, d = inpl()
if d:
    print((2*n-2*d)*(m-1)/n**2)
else:
    print((m-1)/n)