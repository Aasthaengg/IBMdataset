n,k=map(int,input().split())
n+=1
c=0
for b in range(k+1,n):
  c+=n//b*(b-k)
  if k==0:
    c-=1
  if n//b*b+k<n:
    c+=n-n//b*b-k
print(c)