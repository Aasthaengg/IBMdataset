l=[0]*(10**5)
for i in range(1,10**5+1):
  for j in range(2,int(i**0.5)+1):
    if i%j==0:
      break
  else:
    l[i-1]=1
  
d=[0]*(10**5)
t=3
while t<=10**5:
  if l[t-1]==1 and l[(t-1)//2]==1:
    d[t-1]=1
  t+=2

r=[0]*(10**5+1)
for i in range(10**5):
  r[i+1]=r[i]+d[i]
  

q=int(input())
for i in range(q):
  a,b=map(int,input().split())
  print(r[b]-r[a-1])
