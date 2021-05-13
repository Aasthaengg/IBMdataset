n,m=map(int,input().split())
def divisor(n):
  ass=[]
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      ass.append(i)
      if i!=n//i:ass.append(n//i)
  return ass
ans=0
for i in divisor(m):
  if m//i>=n:ans=max(ans,i)
print(ans)