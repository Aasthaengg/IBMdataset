import math
x = int(input())
if x == 1 or x== 2 or x==3:
  print(1)
  exit()

s = math.floor(math.sqrt(x))

def l(k,p):
  q = int(math.floor(math.log(p)/math.log(k)))
  if k ** (1+q) <= p:
    return(1+q)
  else:
    return(q)

ans = 0
for i in range(2,s+1):
  ans = max(ans, i ** l(i,x))
  if ans == x:
    print(x)
    exit()
  
print(ans)
