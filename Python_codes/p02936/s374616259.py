import collections
N,Q=map(int,input().split())
arr=[[] for i in range(N)]

for i in range(N-1):
    a,b=map(int,input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

lis=[0]*N
for i in range(Q):
    a,b=map(int,input().split())
    lis[a-1]+=b


#print(lis)
vist=[0]*N
d=collections.deque()
d.append(0)
while d:
    a=d.pop()
    vist[a]=1
    
    for j in arr[a]:
        
        if vist[j]==1:
            continue
        lis[j]+=lis[a]
        d.append(j)
 #   print(a,d,lis,vist)



print(*lis)