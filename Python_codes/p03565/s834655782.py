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

    N, M = len(S), len(T)
    ans = []

    for i in range(N - M + 1):
        ok = True
        s = list(S)
        for j in range(M):
            if S[i + j] == '?':
                s[i + j] = T[j]
            elif S[i + j] != T[j]:
                ok = False
                break
        if ok:
            ans.append(''.join(s).replace('?', 'a'))

    if ans:
        print(min(ans))
    else:
        print('UNRESTORABLE')

    return


if __name__ == '__main__':
    main()
