import sys
def input(): return sys.stdin.readline().rstrip()
from math import gcd

K = int(input())

one = 0
two = 0
three = 0
for i in range(1,K-1):
    for j in range(i+1,K):
        for k in range(j+1,K+1):
            d = gcd(i,j)
            d = gcd(d,k)
            three += d

for i in range(1,K):
    for j in range(i+1,K+1):
        d = gcd(i,j)
        two += d
for i in range(1,K+1):
    one += i

ans = one + two * 6 + three * 6
print(ans)