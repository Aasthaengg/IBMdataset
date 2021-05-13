import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    H = sorted([int(input()) for _ in range(N)])
    ans = 10 ** 10
    for i in range(N - K + 1):
        if H[i + K - 1] - H[i] < ans:
            ans = H[i + K - 1] - H[i]
    print(ans)


if __name__ == '__main__':
    main()
