W,H,x,y = map(int,input().split())
ans = float(W*H)/2.0
ans2 = (x==W/2) and (y==H/2)
print(ans,ans2*1)