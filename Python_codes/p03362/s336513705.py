import math
n=int(input())
def chk(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      return False
  return True
ans=[]
for i in range(2,10000*1000+1):
  if chk(i) and i%5==1:
    ans.append(i)
  if len(ans)>=n:
    break
print(' '.join(map(str,ans)))
