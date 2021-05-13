# 148c

from sys import stdin
import fractions

a, b=map(int, stdin.readline().strip().split())
f=fractions.gcd(a,b)
f2=a*b//f

print(f2)
