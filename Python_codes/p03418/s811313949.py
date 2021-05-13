def main():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())

    if K == 0:
        print(N**2)
        exit()

    ans = 0
    for b in range(K+1, N+1):
        ans += N // b * (b-K) + max(N%b - (K-1), 0)
    print(ans)


if __name__ == '__main__':
    main()
