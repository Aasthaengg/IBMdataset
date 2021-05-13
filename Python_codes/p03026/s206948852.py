import heapq as h

N=int(input())
hen=[[] for i in range(0,N)]
for i in range(0,N-1):
    a,b=map(int,input().split())
    hen[a-1].append(b-1)
    hen[b-1].append(a-1)

c=list(map(int,input().split()))
c.sort(reverse=True)

ans=[-1 for i in range(0,N)]

q=[]
q.append(0)
h.heapify(q)
sub=[]
h.heapify(sub)
count=0
while q!=[]:
    while q!=[]:
        x=h.heappop(q)
        ans[x]=c[count]
        count+=1
        for p in hen[x]:
            if ans[p]==-1:
                h.heappush(sub,p)
        #何らかの操作
        #ここでsubキューに次に使うものを格納
        if q==[]:
            q=sub
            sub=[]
            h.heapify(sub)
            break

print(sum(c)-c[0])
print(*ans)