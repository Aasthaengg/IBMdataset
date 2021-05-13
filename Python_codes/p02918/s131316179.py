def main():
    N, K = map(int, input().split())
    S = input()
    if N == 1:
        print(0)
        return

    # print(N, K, S)
    ans = 0

    # RR...
    if S[0] == 'R' and S[1] == 'R':
        ans += 1

    for i in range(1, N - 1):
        cl = S[i - 1]
        cc = S[i + 0]
        cr = S[i + 1]
        if cc == 'L' and cc == cl:
            ans += 1
        elif cc == 'R' and cc == cr:
            ans += 1

    # ...LL
    if S[N - 1] == 'L' and S[N - 2] == 'L':
        ans += 1

    ans += K * 2
    ans = min(ans, N - 1)
    print(ans)

if __name__ == '__main__':
    main()
