def main():
    N, K = (int(i) for i in input().split())
    ans = 0
    if K == 0:
        return print(N**2)
    for a in range(1, N+1):
        r = N % a
        p = (N - r) // a
        ans += p * max(0, a - K)
        ans += max(0, r - K + 1)
    print(ans)


if __name__ == '__main__':
    main()
