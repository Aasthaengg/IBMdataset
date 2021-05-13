import sys
import os
import math
import bisect

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: x * y / math.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B, Q = il()
    J = [-MAX] + [ii() for _ in range(A)] + [MAX]
    T = [-MAX] + [ii() for _ in range(B)] + [MAX]
    que = [ii() for _ in range(Q)]
    for q in que:
        a = bisect.bisect_left(J, q)
        b = bisect.bisect_left(T, q)
        ret = MAX
        for j in J[a - 1:a + 1]:
            for t in T[b - 1:b + 1]:
                ret = min(ret, abs(j - q) + abs(t - j), abs(t - q) + abs(j - t))
        print(ret)


if __name__ == '__main__':
    main()
