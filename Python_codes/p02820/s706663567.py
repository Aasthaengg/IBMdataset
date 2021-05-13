import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = map(int, readline().split())
    point = list(map(int, readline().split()))
    T = readline().strip()

    T = T.translate(str.maketrans('rsp', '012'))
    T = list(map(int, T))

    hand = [0] * N
    ans = 0
    for i in range(N):
        win = (T[i] - 1) % 3
        if i < K or hand[i - K] != win:
            hand[i] = win
            ans += point[win]
        else:
            hand[i] = -1

    print(ans)
    return


if __name__ == '__main__':
    main()
