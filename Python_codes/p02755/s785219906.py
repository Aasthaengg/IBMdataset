import math

a,b=map(int,input().split())
ans=-1

for i in range(1,10001):
  if math.floor(i*(8/100)) == a and math.floor(i*(10/100)) == b:
    ans=i
    break
    
print(ans)