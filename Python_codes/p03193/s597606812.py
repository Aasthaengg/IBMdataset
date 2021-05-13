N,H,W=map(int,input().split())
board=0
for i in range(N):
    a,b=map(int,input().split())
    if H<=a and W<=b:
        board+=min(a//H,b//W)
print(board)