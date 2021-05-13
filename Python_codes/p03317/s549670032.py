#!python3

# input
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))


def main():
    s = N - K
    k = K - 1
    ans = 1
    ans += s // k
    if s % k != 0:
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
