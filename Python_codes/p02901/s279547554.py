import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
s_readline = sys.stdin.readline

INF = 10**9 + 7

N, M = map(int, readline().split())
key = [()] * M

for i in range(M):
    a, b = map(int, readline().split())
    c = map(int, readline().split())
    num = 0
    for j in c:
        num += 1 << (j - 1)
    key[i] = (num, a)


def solve():

    dp = [INF for _ in range(2**N)]
    dp[0] = 0

    for i in range(M):
        num, a = key[i]
        for j in range(2**N):
            next_num = j | num
            dp[next_num] = min(dp[next_num], dp[j] + a)

    if dp[2**N - 1] == INF:
        ans = -1
    else:
        ans = dp[2**N - 1]

    print(ans)


if __name__ == '__main__':
    solve()
