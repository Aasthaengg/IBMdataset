import sys,heapq
def input():
    return sys.stdin.readline()[:-1]
X,Y,Z,K=map(int,input().split())
A=list(map(lambda x:int(x)*-1,input().split()))
B=list(map(lambda x:int(x)*-1,input().split()))
C=list(map(lambda x:int(x)*-1,input().split()))
h=[]
heapq.heapify(h)
for i in A:
    for j in B:
        heapq.heappush(h,i+j)
m=min(K,len(h))
l=[None]*m
for i in range(m):
    l[i]=heapq.heappop(h)
h=[]
heapq.heapify(h)
for i in l:
    for j in C:
        heapq.heappush(h,i+j)
for i in range(K):
    print(heapq.heappop(h)*-1)