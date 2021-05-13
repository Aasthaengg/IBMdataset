N=int(input())
l=0
r=0
for i in range(1,N+1):
  s=i*(i+1)//2
  if s>=N:
    l=i
    r=s-N
    break
ans=list(range(1,l+1))
if r!=0:
  ans.remove(r)
print(*ans,sep='\n')