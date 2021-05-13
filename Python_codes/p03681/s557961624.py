def main():
    N, M = map(int, input().split())
    if abs(N - M) > 1:
        print(0)
        exit()
    v = 10 ** 9 + 7
    ans = 1
    for n in range(1, N+1):
        ans = (ans * n) % v
    for m in range(1, M+1):
        ans = (ans * m) % v
    if N == M:
        ans = (ans * 2) % v
    print(ans)


if __name__ == '__main__':
    main()
