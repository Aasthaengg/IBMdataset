n=int(input())

a=list(map(int,input().split()))

bit=[0 for _ in range(30)]
b=[]

for x in a:
  y=[0 for _ in range(30)]
  for i in range(30):
    if (x>>i)&1:
      y[i]+=1
      bit[i]+=1
  b.append(y)
     
ans1=[]
for g in b:
  ans=0
  for j in range(30):
    if (bit[j]%2)!=(g[j]):
      ans+=2**j
  ans1.append(str(ans))
  
print(' '.join(ans1))