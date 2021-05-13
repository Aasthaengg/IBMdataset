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
def main2(a,b,c,k):
  a.sort(reverse=True)
  b.sort(reverse=True)
  c.sort(reverse=True)
  al=[]
  for i,x in enumerate(a):
    for j,y in enumerate(b):
      for l,z in enumerate(c):
        if (i+1)*(j+1)*(l+1)<=k:
          al.append(x+y+z)
        else:
          break
  al.sort()
  for _ in range(k):
    print(al.pop())

main2(a,b,c,k)

