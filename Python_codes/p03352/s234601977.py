import sys

input = sys.stdin.buffer.readline
in_n = lambda: int(input())
in_nn = lambda: map(int, input().split())
in_s = lambda: input().rstrip().decode('utf-8')
in_map = lambda: [s == ord('.') for s in input() if s != ord('\n')]

MOD = 10**9 + 7
INF = 8 * 10**18


def main():

    x = in_n()

    dp = [False] * 1100
    dp[1] = True

    for i in range(2, 110):
        for j in range(2, 20):
            now = i**j
            if now <= 1000:
                dp[now] = True
            else:
                break

    for i in range(x, 0, -1):
        if dp[i]:
            print(i)
            break


if __name__ == '__main__':
    main()
