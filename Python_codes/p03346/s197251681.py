def main():
    N = int(input())
    P = [int(input()) for i in range(N)]

    Q = [0]*(N+1)
    for i in range(N):
        Q[P[i]] = i+1

    ans = 1
    pre = Q[1]
    cur = 1
    for q in Q[2:]:
        if pre < q:
            cur += 1
        else:
            ans = max(ans, cur)
            cur = 1
        pre = q
    ans = max(ans, cur)
    print(N - ans)


if __name__ == '__main__':
    main()
