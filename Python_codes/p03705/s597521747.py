n,a,b = map(int,input().split())
print(b*(n-2)-a*(n-2)+1 if b*(n-2)-a*(n-2)+1 > 0 else 0)