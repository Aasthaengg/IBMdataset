H,W,D = map(int,input().split())

A = [[] for _ in range(H)]
Aset = [[] for _ in range(H)]
for i in range(H):
    A[i] = list(map(int,input().split()))
    Aset[i] = set(A[i])

#1,1+D,1+2D,...
#2,2+D,2+2D,...
#...
#D,2D,3D,...
cost = [0]*(H*W+1)
for i in range(1,D+1):
    num = i
    now = None#座標
    while True:
        if num > H*W:
            break
        for row in range(H):
            if num in Aset[row]:
                #print(row)
                ind = A[row].index(num)
                if now == None:
                    now = (ind, row)#x,y
                    cost[num] = 0
                else:
                    cost[num] = cost[num-D] + abs(ind-now[0]) + abs(row-now[1])
                    now = (ind, row)
        num += D

Q = int(input())
for _ in range(Q):
    l, r = map(int,input().split())
    print(cost[r]-cost[l])