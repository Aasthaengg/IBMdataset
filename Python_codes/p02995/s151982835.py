from math import gcd
def calc(a,b,n):
  return b//n-(a-1)//n
def solve():
  A, B, C, D = map(int, input().split())
  ans = B-A+1-calc(A,B,C)-calc(A,B,D)+calc(A,B,C*D//gcd(C,D))
  return ans
print(solve())