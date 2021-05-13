def inpl(): return [int(i) for i in input().split()]
n, m, d = inpl()
print((2 - (d == 0))*(n-d)/(n**2)*(m-1))