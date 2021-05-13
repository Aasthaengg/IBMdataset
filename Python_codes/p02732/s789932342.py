n=int(input())
a=list(map(int,input().split()))
d={}
for b in a:
  if b not in d:
    d[b]=0
  d[b]+=1

ans=0
for c in d:
  ans+=(d[c]*(d[c]-1))//2
  
for k in range(n):
  e=a[k]
  print(ans-(d[e]*(d[e]-1))//2+(d[e]-1)*(d[e]-2)//2)