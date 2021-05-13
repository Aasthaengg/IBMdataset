# maximum sum of minimum
n=int(input())
node={i:[]for i in range(n+1)}
visited=[False for i in range(n+1)]

#尋ねたことがあるかどうか確認するためのリスト
first=0

for _ in range(n-1):
    a,b=map(int,input().split())
    node[a].append(b)
    node[b].append(a)
    if _==0:
        first+=a
        

dictionary=[0 for i in range(n+1)]
#答を格納するためのリスト
clist=list(map(int,input().split()))
clist=sorted(clist,reverse=True)
counter=0
dictionary[first]=clist[0]
K=sum(clist[1:])
from collections import deque
d=deque()
e=deque()
d.append(first)
visited[first]=True
while d:
    for some in d:
        for point in node[some]:
            if visited[point]==False:
                #まだ訪れたことのない頂点にあった場合
                counter+=1
                visited[point]=True
                dictionary[point]=clist[counter]
                e.append(point)
            else:
                pass
    d=e
    e=deque()
print(K)
print(*dictionary[1:])
