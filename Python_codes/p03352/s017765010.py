import math
x = int(input())
if x == 1 or x== 2 or x==3:
  print(1)
  exit()

s = math.floor(math.sqrt(x))

def l(k,p):
    return(int(math.floor(math.log(p)/math.log(k))))

ans = 0
for i in range(2,s+1):
  if i ** (1 + l(i,x)) <= x:
    ans = max(ans, i ** (1+l(i,x)))
  else:
    ans = max(ans, i ** l(i,x))
  if ans == x:
    print(x)
    exit()
  
print(ans)