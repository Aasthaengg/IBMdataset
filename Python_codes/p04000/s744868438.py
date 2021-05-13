from collections import defaultdict

H,W,N=map(int,input().split())
ab=[]
dict=defaultdict(int)
for i in range(N):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            Y=a+y
            X=b+x
            if 0<=Y-1 and Y+1<H and 0<=X-1 and X+1<W:
                dict[(X,Y)]+=1
M=H*W-2*W-2*H+4
v=[0]*10
for i,j in dict.items():
    v[j]+=1
v[0]=M-sum(v[1:])
for i in range(10):
    print(v[i])
