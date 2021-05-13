# C - Subarray Sum
def main():
    N, K, S = map(int, input().split())
    res = [S] * K + [1 if S == 10 ** 9 else S + 1] * (N - K)
    print(*res)


if __name__ == "__main__":
    main()
