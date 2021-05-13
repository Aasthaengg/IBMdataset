import sys
import fractions
input = sys.stdin.readline

MOD = pow(10, 9) + 7
n = int(input())
a = list(map(int, input().split()))

lcm = a[0]
for i in range(n):
    lcm = lcm * a[i] // fractions.gcd(lcm, a[i])

b = []
for i in range(n):
    b.append(lcm // a[i])

print(sum(b) % MOD)