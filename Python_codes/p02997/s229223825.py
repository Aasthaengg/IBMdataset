import itertools
N,K=map(int,input().split())
c=(N-1)*(N-2)//2
if c<K:
    print(-1)
    exit()
Edges=[]
for i in range(1,N):
    Edges.append([1,i+1])
cnt=0
for x in itertools.combinations(range(1,N),2):
    if cnt==c-K:
        break
    Edges.append([x[0]+1,x[1]+1])
    cnt+=1
print(len(Edges))
for x,y in Edges:
    print(x,y)