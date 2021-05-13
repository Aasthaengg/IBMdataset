from collections import defaultdict, deque, Counter
import sys
input = sys.stdin.readline


def getPrimes(n):
    isPrime = [True] * n
    ret = []
    for p in range(2, n):
        if not isPrime[p]:
            continue
        ret.append(p)
        for i in range(p, n, p):
            isPrime[i] = False
    return ret


def main():
    N = int(input())
    P = getPrimes(N)
    C = Counter()

    for i in range(1, N + 1):
        cnt = Counter()
        for p in P:
            while i % p == 0:
                i //= p
                cnt[p] += 1
        C += cnt

    d = {3: 0, 5: 0, 15: 0, 25: 0, 75: 0}
    for k in d.keys():
        for v in C.values():
            if v >= k - 1:
                d[k] += 1

    ans = 0
    ans += (d[5] * (d[5] - 1) // 2) * (d[3] - 2)
    ans += d[15] * (d[5] - 1)
    ans += d[25] * (d[3] - 1)
    ans += d[75]
    print(ans)


if __name__ == '__main__':
    main()
