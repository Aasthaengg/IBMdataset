import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
from itertools import product
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, M = map(int, readline().split())
    S = []
    for _ in range(M):
        k, *s = map(int, readline().split())
        S.append(s)
    P = list(map(int, readline().split()))
    ans = 0

    for switch in product((0,1),repeat=N):
        for i, s in enumerate(S):
            tmp = 0
            for k in s:
                tmp ^= switch[k-1]
            if tmp==P[i]:
                continue
            else:
                break
        else:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()

