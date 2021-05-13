from sys import stdin
import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

n,m = [int(x) for x in stdin.readline().rstrip().split()]

if lcm(n,m) == n:
    print(-1)
else:
    print(n)

