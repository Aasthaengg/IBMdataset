n,k=map(int,input().split())
lst=sorted([list(map(int,input().split())) for _ in range(n)])

cnt=0
sm=0
for i in range(n):
    if sm<k:
        cnt+=1
    sm+=lst[i][1]
print(lst[cnt-1][0])