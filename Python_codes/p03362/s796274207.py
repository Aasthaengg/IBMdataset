n=int(input())
def prime(INF=10**6+1):
  p=[1]*INF
  for i in range(2,INF):
    if p[i]:
      for j in range(2*i,INF,i):p[j]=0
  p[0],p[1]=0,0
  return p
p=prime()
a=[]
cnt=0
for i in range(10**6+1):
  if p[i] and i%5==1:
    a+=[i]
    cnt+=1
  if cnt==n:break
print(*a)