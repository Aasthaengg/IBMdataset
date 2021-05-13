import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = [0] * N
    for i in range(N):
        S[i] = readline().strip()
    M = int(readline())
    T = [0] * M
    for i in range(M):
        T[i] = readline().strip()

    c1 = Counter(S)
    c2 = Counter(T)

    ans = 0
    for k, v in c1.items():
        if ans < v - c2[k]:
            ans = v - c2[k]

    print(ans)
    return


if __name__ == '__main__':
    main()
