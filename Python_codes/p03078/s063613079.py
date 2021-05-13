x,y,z,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

from heapq import heappop,heappush,heapify
def main1(a,b,c,k):
  ans=[]
  for x in a:
    for y in b:
      ans.append(-x-y)
  ans.sort()
  ans=ans[:k] if len(ans)>=k else ans+[0]*(k-len(ans))
  ans1=[]
  for z in c:
    for xy in ans:
      heappush(ans1,xy-z)
  for _ in range(k):
    print(-heappop(ans1))
main1(a,b,c,k)

