import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = -float("inf")
    for t in range(min(N, K) + 1):
        s = K - t
        for l in range(t + 1):
            r = t - l
            gem = V[:l]
            gem += V[-r:] if r != 0 else []
            gem.sort()
            value = sum(gem)
            for i in range(min(s, t)):
                if gem[i] < 0:
                    value -= gem[i]
                else:
                    break
            ans = max(ans, value)

    print(ans)


if __name__ == "__main__":
    main()
