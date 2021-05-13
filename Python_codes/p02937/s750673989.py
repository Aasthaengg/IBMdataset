import sys
from bisect import bisect_right

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    T = readline().strip()
    N = len(S)
    M = len(T)

    SS = S + S

    A = [False] * 26
    for c in S:
        A[ord(c) - 97] = True

    for c in T:
        if not A[ord(c) - 97]:
            print(-1)
            return

    B = [[] for _ in range(26)]
    for i, c in enumerate(SS):
        B[ord(c) - 97].append(i)

    i = B[ord(T[0]) - 97][0]
    ans = i + 1
    for c in T[1:]:
        j = B[ord(c) - 97][bisect_right(B[ord(c) - 97], i)]
        ans += j - i
        if j < N:
            i = j
        else:
            i = j - N

    print(ans)
    return


if __name__ == '__main__':
    main()
