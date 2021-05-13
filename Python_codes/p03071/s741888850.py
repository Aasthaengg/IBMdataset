n,m = map(int,input().split())
print(n+(n-1) if n > m else m+(m-1) if n < m else n+m)