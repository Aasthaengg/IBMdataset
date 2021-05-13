from collections import defaultdict

N,K=map(int,input().split())
d=defaultdict(int)
for i in range(N):
    a,b=map(int,input().split())
    d[a]+=b

d=d.items()
d=sorted(d,key=lambda x:x[0])

cnt=0
for key,value in d:
    cnt+=value
    if cnt>=K:
        print(key)
        exit()