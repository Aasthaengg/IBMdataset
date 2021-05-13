def main():
    N, K = map(int, input().split())

    if K % 2 != 0:
        ans = (N // K)**3
    else:
        n = N // K
        if (n + 0.5) * K <= N:
            ans = (n + 1)**3 + n**3
        else:
            ans = 2 * n**3

    print(ans)


main()
