# coding: utf-8
# Your code here!
#途中

H,W,D=map(int,input().split())

A=[]
for i in range(H):
    A.append(list(map(int,input().split())))

loc=[[0,0] for i in range(W*H)]

#print(loc)

for i in range(H):
    for j in range(W):
        loc[A[i][j]-1][0]=i
        loc[A[i][j]-1][1]=j
        #print(loc)
#print(loc)

cost=[[0]*((H*W)//D) for i in range(D)]

for i in range((H*W)%D):
    cost[i].append(0)

for i in range(D):
    pass
    count=1
    temp=i
    while temp+D<(H*W):
        temp=i+D*count
        cost[temp%D][temp//D]=abs(loc[temp][0]-loc[temp-D][0])+abs(loc[temp][1]-loc[temp-D][1])+cost[temp%D][temp//D-1]
        count+=1
        #print(cost)
cost[-1]=[0]+cost[-1]

Q=int(input())
for _ in range(Q):
    x,y=map(int,input().split())
    #print(cost[x%D-1][x//D-1])
    print(cost[y%D-1][y//D]-cost[x%D-1][x//D])

#print(cost)

