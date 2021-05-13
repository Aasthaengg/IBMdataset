m,n = map(int,input().split())
if m == n:print(m+n)
else:print(max(m,n)*2-1)