n,k,*a=map(int,open(0).read().split())
s,m=sum(a),1
for i in sum([[s//i,i]for i in range(1,int(s**.5)+1)if s%i<1],[]):
  p=[0]+sorted(j%i for j in a)
  for j in range(n):p[j+1]+=p[j]
  f=t=0
  for j in range(n):
    f|=t==p[~j]<=k
    t+=i-p[~j]+p[-j-2]
  m=max(m,i*f)
print(m)