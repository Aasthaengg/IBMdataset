import sys
input = sys.stdin.readline

n = int(input())

import math

if n%2 == 1:
    print(0)
    exit()

k = 0
while n - 2*5**k >= 0:
    k += 1
k -= 1

ans = 0
for i in range(1, k+1):
    ans += n//(2*5**i)

print(ans)
