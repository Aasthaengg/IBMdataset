import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, D, A = NMI()
    M = [NLI() for _ in range(N)]
    M.sort()
    maxj = [0] * N
    j = 0
    for i in range(N):
        while j < N-1:
            if M[j+1][0] <= M[i][0] + D*2:
                j += 1
            else:
                break
        maxj[i] = j
    S = [0]*(N+1)
    ans = 0
    for i in range(N):
        x = M[i][0]
        hp = M[i][1] - S[i]
        need = max((hp-1) // A + 1, 0)
        ans += need
        S[i] += need * A
        S[maxj[i]+1] -= need * A
        S[i+1] += S[i]

    print(ans)





if __name__ == "__main__":
    main()