import sys
input=sys.stdin.readline #文字列入力はするな！！
import heapq
n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    a[i]*=-1
a=sorted(a)
for i in range(m):
    h=-heapq.heappop(a)
    h=h//2
    heapq.heappush(a,-h)
print(-sum(a))

