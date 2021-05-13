N,M=map(int,input().split())
stu=[0 for i in range(N)]
che=[0 for j in range(M)]

for i in range(N):
    stu[i]=list(map(int,input().split()))

for j in range(M):
    che[j]=list(map(int,input().split()))

for s in range(N):
    x=[]
    a,b=stu[s]
    for t in range(M):
        c,d=che[t]
        x.append(abs(a-c)+abs(b-d))
    num=x.index(min(x))
    print(num+1)