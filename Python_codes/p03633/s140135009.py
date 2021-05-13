from math import gcd
answer = 1
for _ in range(int(input())):
  T = int(input())
  answer = answer*T//gcd(answer,T)
print(answer)