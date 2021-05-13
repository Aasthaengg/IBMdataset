import math
a, b, c, d = map(int, input().split())
e = c*d//math.gcd(c,d)
def ko(a,b,c):
  x = b//c-a//c
  if a%c==0:
    x+=1
  return(x)
print(b-a+1-ko(a,b,c)-ko(a,b,d)+ko(a,b,e))