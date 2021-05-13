import sys
input = sys.stdin.readline

N=int(input())
mod = int(1e9+7)
p = 1
for i in range(1,N+1):
    p *= i
    p %= mod
print(p)

