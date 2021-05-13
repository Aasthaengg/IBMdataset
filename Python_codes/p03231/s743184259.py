import sys
from fractions import gcd


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    N, M = map(int, input().split())
    S = input()
    T = input()
    g = gcd(M, N)
    n = N // g
    m = M // g
    s = []
    t = []
    for i in range(N):
        if i % n == 0:
            s.append(S[i])
    for j in range(M):
        if j % m == 0:
            t.append(T[j])
    for x, y in zip(s, t):
        if x != y:
            print(-1)
            return
    print(M * N // g)


if __name__ == "__main__":
    main()
