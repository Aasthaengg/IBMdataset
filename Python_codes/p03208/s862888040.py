# coding: utf-8


def main():
    N, K = map(int, input().split())
    H = sorted([int(input()) for _ in range(N)])
    ans = min([H[i + K - 1] - H[i] for i in range(N - K + 1)])

    print(ans)

if __name__ == "__main__":
    main()
