A,B,C,D=map(int,input().split())
def f(x):
  return B//x-(A-1)//x
import math
E=int(C*D/math.gcd(C,D))
print(B-A+1-f(C)-f(D)+f(E))