import heapq

n,k=map(int,input().split())
v=list(map(int,input().split()))
s=-10**7-1

if n>k:
    for l in range(k//2+1):
        for i in range(k+1-l):
            d=v[:i]
            d.extend(v[(n-k+l+i):])
            heap=heapq.heapify(d)
            res=sum(d)
            for j in range(l):
                t=heapq.heappop(d)
                if t<0:
                    res-=t
                else:
                    break
            if s<res:
                s=res
else:
    for l in range(n+1):
        for i in range(n-l+1):
            d=v[:i]
            d.extend(v[(l+i):])
            heap=heapq.heapify(d)
            res=sum(d)
            for j in range(k-(n-l)):
                if not d:
                    break
                t=heapq.heappop(d)
                if t<0:
                    res-=t
                else:
                    break
            if s<res:
                s=res

        
if s<0:
    print(0)
else:
    print(s)
        
