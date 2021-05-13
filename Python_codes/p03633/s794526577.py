from fractions import gcd
a = 1

for n in range(int(input())):
  T = int(input())
  a = a*T//gcd(a,T)

print(a)