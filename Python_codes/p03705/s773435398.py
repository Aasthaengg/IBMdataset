n,a,b = map(int, input().split())
l,r = a*(n-1)+b, b*(n-1)+a
print(r-l+1 if r-l+1 > 0 else 0)