import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if (c % gcd(a, b)) == 0:
    print('YES')
else:
    print('NO')
