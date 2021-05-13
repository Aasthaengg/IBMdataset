W,H,x,y = map(int,input().split())
ans = W * H / 2
if x * 2 == W and y * 2 == H:
    flg = 1
else:
    flg = 0
print(ans,flg)