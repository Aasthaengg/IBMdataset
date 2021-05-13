#19:38
#20:19

H,W,D = map(int,input().split())
MAX = H*W
A = [list(map(int,input().split())) for i in range(H)]
Point = [0]*(MAX+1)
for h in range(H):
    for w in range(W):
        Point[A[h][w]] = (h,w)
K = []
for i in range(1,D+1):
    List = []
    n = i
    h,w = Point[n]
    cost = 0
    while n<=MAX:
        y,x = Point[n]
        cost += abs(h-y)+abs(w-x)
        List.append(cost)
        h,w = y,x
        n+=D
    K.append(List)
Q = int(input())
for i in range(Q):
    L,R = map(int,input().split())
    a,l,r = (L-1)%D,(L-1)//D,(R-1)//D
    print(K[a][r]-K[a][l])