import sys
from fractions import gcd
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def lcm(a, b):
    return a*b//gcd(a, b)

def main():
    N = ii()
    T = [ii() for _ in range(N)]
    ans = 1
    for i in range(N):
        ans = lcm(ans, T[i])
    print(ans)


if __name__ == '__main__':
    main()
