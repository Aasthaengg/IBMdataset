W,a,b = map(int,input().split())
print(0 if abs(b-a) < W else abs(b-a)-W)