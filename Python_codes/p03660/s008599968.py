from bisect import *
from collections import *
N=int(input())
AB=[map(int,input().split()) for i in range(N-1)]
data=[[] for i in range(N+1)]
for a,b in AB:
    data[a].append(b)
    data[b].append(a)
stack=deque([[1,0]])
visited=set([1])
flag=0
while stack :
    a,m=stack.popleft()
    for p in data[a]:
        if p==N:
            flag=1
            break
        if not p in visited:
            visited.add(p)
            stack.append([p,m+1])
    if flag:
        break

M=m//2
countFennec=0
countSnuke=0
visited=set([1,N])
stackSnuke=deque([[N,0]])
while stackSnuke:
    a,m=stackSnuke.popleft()
    if m>=M:
        stackSnuke.append([a,m])
        break
    for p in data[a]:
        if not p in visited:
            countSnuke+=1
            visited.add(p)
            stackSnuke.append([p,m+1])

stackFennec=deque([[1,0]])
while stackFennec:
    a,m=stackFennec.popleft()
    for p in data[a]:
        if not p in visited:
            countFennec+=1
            visited.add(p)
            stackFennec.append([p,m+1])

while stackSnuke:
    a,m=stackSnuke.popleft()
    for p in data[a]:
        if not p in visited:
            countSnuke+=1
            visited.add(p)
            stackSnuke.append([p,m+1])


if countFennec>countSnuke:
    print("Fennec")
else:
    print("Snuke")
