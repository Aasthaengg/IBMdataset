import sys
import fractions
def lcm(a, b):
    return abs(a*b) // fractions.gcd(a, b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
c=2
while a[0]%c==0:
  c=c*2
c=c//2
fail=0
for i in range(n):
  if a[i]%c!=0:
    fail=1
  if a[i]%(2*c)==0:
    fail=1
if fail==1:
  print(0)
  sys.exit()
A=1
for i in range(n):
  A=lcm(A,a[i])
print(2*m//A-2*m//(2*A))