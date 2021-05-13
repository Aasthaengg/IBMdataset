H,W,D=map(int, input().split())
A=[]
for h in range(H):
    a=list(map(int, input().split()))
    A.append(a)

idx=[0]*(H*W)
for h in range(H):
    for w in range(W):
        num=A[h][w]
        idx[num-1]=[h+1,w+1]
acum=[0]*(H*W+1)
for i in range(1,H*W+1):
    if i-D<=0:
        acum[i]=sum(idx[i-1])
    else:
        prex,prey=idx[i-1-D]
        nexx,nexy=idx[i-1]
        acum[i]=acum[i-D]+abs(nexx-prex)+abs(nexy-prey)
#print(acum)


Q=int(input())
for i in range(Q):
    l,r=map(int, input().split())
    print(acum[r]-acum[l])
