import bisect
N,M=map(int,input().split())
P=[]
Y=[]
li=[[] for i in range(N)]

for i in range(M):
    p,y=map(int,input().split())
    li[p-1].append(y)#p市の集合に追加
    P.append(p)
    Y.append(y)

for i in range(N):
    li[i].sort()

for p,y in zip(P,Y):
    zenhan="0"*(6-len(str(p)))+str(p)
    x=bisect.bisect_left(li[p-1], y)+1
    kouhan="0"*(6-len(str(x)))+str(x)
    print(zenhan+kouhan)


