W, a, b = map(int,input().split())
print(0 if max(a,b)-W-min(a,b)<0 else max(a,b)-W-min(a,b))