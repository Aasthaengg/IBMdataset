import sys
from itertools import islice


def resolve(in_):
    H, N = map(int, next(in_).split())
    AB = tuple(tuple(map(int, line.split())) for line in islice(in_, N))
    
    dp = [1 << 31] * (H + 1)
    dp[0] = 0

    for i in range(H):
        for a, b in AB:
            ia = min(H, i + a)
            dp[ia] = min(dp[ia], dp[i] + b)

    return dp[H]


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
