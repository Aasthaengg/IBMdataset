f = lambda a, b, x: int(a*x/b)-a*int(x/b)
a, b, n = map(int, input().split())
print(f(a, b, min(b-1,n)))