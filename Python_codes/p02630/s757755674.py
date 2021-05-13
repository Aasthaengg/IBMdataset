n=int(input())
a=list(map(int,input().split()))
num=[0]*100005
ans=sum(a)

for _ in a:
  num[_-1]+=1

q=int(input())

for i in range(q):
  b,c=map(int,input().split())
  
  if b<=c:
    ans+=(abs(c-b))*num[b-1]
    
  else:
    ans-=(abs(c-b))*num[b-1]
    
  print(ans)
  
  num[c-1]+=num[b-1]
  num[b-1]=0