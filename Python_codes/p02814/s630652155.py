from math import gcd

N,M = map(int,input().split())

A = list(map(int,input().split()))

d = 1
a = A[0]
while a % 2 == 0:
    d *= 2
    a //= 2

if not all((a//d)%2 != 0 and a%d == 0 for a in A):
    print(0)
    exit()

A = [a//d for a in A]
g = 1
for a in A:
    g = g*a//gcd(g,a)

g *= d//2

x = M//g

print((x+1)//2)