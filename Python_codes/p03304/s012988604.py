n,m,d = map(int,input().split())
a = n if d == 0 else 2*(n-d)
print(a/(n**2)*(m-1))