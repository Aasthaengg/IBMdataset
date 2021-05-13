import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = map(int, readline().split())
    R, S, P = map(int, readline().split())
    T = readline().strip()

    T = [int(c) for c in T.translate(str.maketrans('rsp', '012'))]

    point = [R, S, P]
    hand = [0] * N

    ans = 0
    for i, com in enumerate(T):
        win = (com - 1) % 3
        if i >= K and win == hand[i - K]:
            hand[i] = -1
        else:
            hand[i] = win
            ans += point[win]

    print(ans)
    return


if __name__ == '__main__':
    main()
