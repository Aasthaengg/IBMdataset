n=int(input())
a=list(map(int,input().split()))
q=int(input())
sum1=sum(a)
d={}
for x in range(n):
  s=a[x]
  if s not in d:
    d[s]=0
  d[s]+=1

for y in range(q):
  h,g=map(int,input().split())
  if h in d:
    r=d[h]
    sum1=sum1-r*h
    
    if g not in d:
      d[g]=0
    d[g]+=r
    sum1+=r*g
    d[h]=0
    
  print(sum1)