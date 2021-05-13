import sys, os, math, bisect, itertools, collections, heapq, queue
from decimal import Decimal

# import fractions

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)
# lcm = lambda x, y: (x * y) // fractions.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    # エラトステネスの篩で、
    # 2 から 10^5までの素数を列挙
    limit = 10 ** 5 + 1
    prime = [False if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 else True for n in range(limit)]
    prime[0] = prime[1] = False
    prime[2] = prime[3] = prime[5] = True
    for p in range(3, limit, 2):
        if math.sqrt(limit) < p:
            break
        for q in range(p ** 2, limit, p):
            prime[q] = False

    # 累積和
    # 2017に似た数字の数を求めておく
    cnt = [0] * limit
    for n in range(len(cnt)):
        if prime[n] and prime[(n + 1) // 2]:
            cnt[n] = 1
    for n in range(1, len(cnt)):
        cnt[n] += cnt[n - 1]

    # 回答
    Q = ii()
    for q in range(Q):
        l, r = il()
        print(cnt[r] - cnt[l - 1])


if __name__ == '__main__':
    main()
