import sys, fractions

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))

lcm = 1
for a in A:
    lcm = (lcm * a) // fractions.gcd(lcm, a)

lcm -= 1
res = 0
for a in A:
    res += lcm % a

print(res)
