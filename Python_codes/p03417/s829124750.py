n,m=map(int,input().split())
n,m = max(n,m),min(n,m)
print((n-2)*(m-2) if m>=3 else(0 if 2 in (n,m) else(1 if n==m else n-2)))