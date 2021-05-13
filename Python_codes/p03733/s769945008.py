import sys

input = sys.stdin.readline


def main():
    N, T = map(int, input().split())
    t = list(map(int, input().split()))

    ans = T * N
    for i in range(N - 1):
        diff = t[i + 1] - t[i]
        if diff < T:
            ans -= T - diff

    print(ans)


if __name__ == "__main__":
    main()
