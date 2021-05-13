import math
n = int(input())
ta = [list(map(int, input().split())) for i in range(n)]
T,A = 1,1
for t,a in ta:
  mul = max(-(-A//a), -(-T//t))
  T,A = t * mul,a * mul
print(T+A)
