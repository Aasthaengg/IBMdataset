import sys
from fractions import gcd
from functools import reduce
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def main():
    N = int(readline())
    T = []
    for _ in range(N):
        T.append(int(readline()))
    ans = lcm_list(T)
    print(ans)
if __name__ == '__main__':
    main()