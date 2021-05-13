W,H,x,y = map(int,input().split())
cnt = 0
if 2*x == W and 2*y == H:
    cnt = 1
print(W*H*0.5,cnt)