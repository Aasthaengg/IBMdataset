def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K == 2:
        print(N - 1)
    else:
        ans = 10**10
        for k in range(K):
            v = 0
            if k > 0:
                v += 1
            v += (N - k) // (K - 1)
            if (N - k) % (K - 1) > 1:
                v += 1
            if v < ans:
                ans = v
        print(ans)


if __name__ == '__main__':
    main()
