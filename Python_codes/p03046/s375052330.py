def main():
    M, K = map(int, input().split())
    N = 2**M
    if M == 1:
        if K == 0:
            print(*[0, 0, 1, 1])
        else:
            print(-1)
        return
    if K >= N:
        print(-1)
        return
    ans = [x for x in range(N) if x != K]
    ans = ans + [K] + ans[::-1] + [K]
    print(*ans)


if __name__ == "__main__":
    main()
