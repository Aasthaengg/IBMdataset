import heapq  # heapqライブラリのimport
N,M=map(int,input().split())
lst=list(map(int,input().split()))
for i in range(N):
 lst[i]=(-lst[i],1)
for i in range(M):
 B,C=map(int,input().split())
 lst.append((-C,B))
heapq.heapify(lst)  # リストを優先度付きキューへ
ans=0
while N>0 :
 a=heapq.heappop(lst)
 ans+=a[0]*a[1]
 N-=a[1] 
ans+=a[0]*N
print((-1)*ans)
