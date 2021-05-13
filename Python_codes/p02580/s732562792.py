import itertools

H,W,M=map(int,input().split())
d={}
nh=[0]*H
nw=[0]*W
for _ in range(M):
    h,w=map(int,input().split())
    h-=1
    w-=1
    d[(h,w)]=1
    nh[h]+=1
    nw[w]+=1
hmax=max(nh)
wmax=max(nw)
is_h=[i for i in range(H) if nh[i]==hmax]
is_w=[i for i in range(W) if nw[i]==wmax]

for i_h,i_w in itertools.product(is_h,is_w):
    if (i_h,i_w) not in d:
        print(hmax+wmax)
        break
else:
    print(hmax+wmax-1)