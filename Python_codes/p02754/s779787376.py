n, a, b = map(int,input().split())
m = n//(a+b)
if m*(a+b) + a <= n:
    print(a*(m+1))
else:
    print(n-b*m)