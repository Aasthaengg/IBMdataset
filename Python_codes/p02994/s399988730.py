n, l = (int(xi) for xi in input().split())

a = int(n*(l-1)+n*(n+1)/2)

# print(a)
if 0<1-l<n+1: print(a)
if 1-l<1: print(a-(l+1-1))
if n<1-l: print(a-(l+n-1))
