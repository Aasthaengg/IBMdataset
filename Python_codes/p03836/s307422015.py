import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    sx, sy, tx, ty = map(int, readline().split())

    S = [0] * 4
    S[0] = 'U' * (ty - sy + 1)
    S[1] = 'R' * (tx - sx + 1)
    S[2] = 'D' * (ty - sy + 1)
    S[3] = 'L' * (tx - sx + 1)
    S = ''.join(S)

    ans = ''.join([S[1:], S[:1], S[-1:], S[:-1]])
    print(ans)

    return


if __name__ == '__main__':
    main()
