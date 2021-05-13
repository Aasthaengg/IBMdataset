import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

input_n = lambda: int(readline())
input_nn = lambda: map(int, readline().split())
input_s = lambda: readline().rstrip().decode('utf-8')
input_ss = lambda: readline().rstrip().decode('utf-8').split()

mod = 10 ** 9 + 7


def judge(a, b, c, k):

    ret = False
    ret |= (b == 0 and c == 2 and k == 1)
    ret |= (b == 0 and c == 1 and k == 2)
    ret |= (b == 2 and c == 0 and k == 1)
    ret |= (a == 0 and b == 2 and k == 1)
    ret |= (a == 0 and c == 2 and k == 1)

    return not ret


def main():

    N = input_n()
    dp = np.full((4, 4, 4), 1, np.int32)
    dp[0, 2, 1] = 0
    dp[0, 1, 2] = 0
    dp[2, 0, 1] = 0

    for n in range(N - 3):
        next_dp = np.zeros((4, 4, 4), np.int32)
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for k in range(4):
                        if judge(a, b, c, k):
                            next_dp[b, c, k] += dp[a, b, c]
                            next_dp[b, c, k] %= mod
        dp = next_dp

    print(dp.sum() % mod)


if __name__ == '__main__':
    main()
