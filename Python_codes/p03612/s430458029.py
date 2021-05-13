N=int(input())
p=list(map(int,input().split()))
t=0
for i in range(N):
  if i!=N-1:
    if p[i]==i+1:
      s=p[i+1]
      p[i]=s
      p[i+1]=i+1
      t+=1
  else:
    if p[i]==i+1:
      u=p[i-1]
      p[i]=u
      p[i-1]=i+1
      t+=1
print(t)