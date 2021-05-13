p={}
H,W,D=map(int,input().split())

for h in range(H):
    A=list(map(int,input().split()))
    for w in range(W):
        p[A[w]]=[h,w]

Series=[]
for d in range(1,D+1):
    distance=[0]
    while d+D<=H*W:
        distance.append(distance[-1]+abs(p[d][0]-p[d+D][0])+abs(p[d][1]-p[d+D][1]))
        d+=D
    Series.append(distance)

#print(Series)
Q=int(input())
Ans=[]
for q in range(Q):
    l,r=map(int,input().split())
    if l%D==0:
        Idx=D-1
    else:
        Idx=l%D-1
    Ans.append(Series[Idx][(r-Idx-1)//D]-Series[Idx][(l-Idx-1)//D])

for i in range(Q):
    print(Ans[i])