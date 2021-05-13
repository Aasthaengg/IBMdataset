from itertools import groupby
import heapq

X=input()
N=len(X)
X=[X[i] for i in range(0,N)]
X=groupby(X)
data=[]
i=0
for key,group in X:
    g=len(list(group))
    data.append((i,key,g))
    i+=1

if data[0][1]=='T':
    data=data[1:]
if data[-1][1]=='S':
    data=data[:len(data)-1]


heapq.heapify(data)
left=0
ans=0
while data:
    S=heapq.heappop(data)
    T=heapq.heappop(data)
    s=S[2]+left
    t=T[2]
    if s>=t:
        left=s-t
        ans+=t
    else:
        left=0
        ans+=s

print(N-2*ans)