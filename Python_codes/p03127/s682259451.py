from fractions import gcd

N = int(input())
As = list(map(int, input().split()))

rlt = As[0]

for a in As[1:]:
  rlt = gcd(a,rlt)
  
print(rlt)