n,k=map(int,input().split())
a=list(map(int,input().split()))

d=[0 for i in range(40)]
for i in a:
  for j in range(40):
    d[j]+=1 if i&(2**j) else 0
s=[]
ss=0
for i in range(40):
  ss+=(2**i)*max(d[i],n-d[i])
  s.append(ss)
s.append(0)
mx=0
isum=0
for i in range(39,-1,-1):
  if k&(2**i):
    mx=max(mx,isum+(2**i)*d[i]+s[i-1])
    isum+=(2**i)*(n-d[i])
  else:
    isum+=(2**i)*d[i]
mx=max(mx,isum)
print(mx)