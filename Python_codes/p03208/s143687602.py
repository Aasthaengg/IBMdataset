def main():
    n, k = map(int, input().split())
    H = [int(input()) for _ in range(n)]
    H.sort()
    ans = 10 ** 9 + 2
    for i in range(n - k + 1):
        ans = min(ans, H[i + k - 1] - H[i])
    print(ans)

if __name__ == '__main__':
    main()
