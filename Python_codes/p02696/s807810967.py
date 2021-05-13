a,b,n = list(map(int, input().split()))
x = min(n,b - 1)
print(int(a*x/b)-a*int(x/b))