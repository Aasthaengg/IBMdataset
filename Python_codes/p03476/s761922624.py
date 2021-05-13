import math
import itertools

def get_prime(n):
    if n<=1:
      return []
    prime=[2]
    limit=int(math.sqrt(n))
    
    data=[i+1 for i in range(2,n,2)]
    while limit>data[0]:
      prime.append(data[0])
      
      data=[j for j in data if j % data[0]!=0]
      
    return prime+data

xx=get_prime(100000)

xxx=[False]*100001

for i in xx:
  xxx[i]=True

xxxx=[False]*100001

for i in xx:
  xxxx[i]=True

for i in range(1,100001):
  if xxx[i]==True:
    if xxxx[(i+1)//2]==False:
      xxx[i]=False

q=int(input())

for i in range(100001):
  if xxx[i]==True:
    xxx[i]=1
  else:
    xxx[i]=0
    
xxx=list(itertools.accumulate(xxx))
    

for i in range(q):
  l,r=map(int,input().split())
  print(xxx[r]-xxx[l-1])