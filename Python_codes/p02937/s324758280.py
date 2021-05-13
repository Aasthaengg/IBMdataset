import sys

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

    B = [[-1] * N for _ in range(26)]
    for c in set(T):
        code = ord(c) - 97
        row = B[code]

        left = right = 0
        while True:
            right = SS.find(c, left + 1)
            if right < N:
                row[left:right] = [right] * (right - left)
                left = right
            else:
                row[left:N] = [right] * (N - left)
                break

    ans = i = S.find(T[0])
    for c in T[1:]:
        j = B[ord(c) - 97][i]
        ans += j - i
        if j < N:
            i = j
        else:
            i = j - N

    print(ans + 1)
    return


if __name__ == '__main__':
    main()
