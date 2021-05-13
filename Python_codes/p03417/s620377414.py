n,m = map(int, input().split())
print(0 if n==2 or m==2 else max(n-2,1)*max(m-2,1))