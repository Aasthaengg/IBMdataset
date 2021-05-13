N,X,Y = map(int,input().split())
cnt = 0
for i in range(N):
    x,y = map(int,input().split())
    if x >= X and y >= Y:
        cnt += 1
print(cnt)