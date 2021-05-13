import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    x, y = map(int, readline().split())

    S = S.split('T')
    x0 = len(S[0])
    X = [len(s) for s in S[2::2]]
    Y = [len(s) for s in S[1::2]]

    def solve(vec, p0, p):
        s = {p0}
        for v in vec:
            s, s_prev = set(), s
            for w in s_prev:
                s.add(w + v)
                s.add(w - v)
        return p in s

    if solve(X, x0, x) and solve(Y, 0, y):
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
