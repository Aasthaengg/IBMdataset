import sys
import math

stdin = sys.stdin

nm = lambda: map(int, stdin.readline().split())

a, b = nm()

n = math.gcd(a,b)

count = 1 # 1
for i in range(2, int(n**(1/2))+1):
    if n%i ==0:
        count +=1
        while n%i == 0:
            n = n/i
    if n ==1:
        break
if n != 1:
    count += 1

print(count)