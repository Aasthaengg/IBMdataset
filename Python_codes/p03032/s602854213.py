import heapq

res=0
n,k=map(int,input().split())
v=list(map(int,input().split()))
r=min(n,k)
for a in range(r+1):#操作Aの回数
    for b in range(r-a+1):#Bの回数
        d=v[:a]
        d.extend(v[n-b:])
        s=sum(d)
        heapq.heapify(d)

        l=k-(a+b) #捨てる回数print(d)
        for _ in range(l):
            if not d:
              break
            t=heapq.heappop(d)
            if t<0:
               s-=t
            else:
                break
        if s>res:
            res=s
print(res) 
