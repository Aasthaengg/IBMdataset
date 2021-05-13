n,a,b = map(int,input().split())
ma = min(a,b)
mi = max(ma - (n - max(a,b)), 0)
print(ma,mi)