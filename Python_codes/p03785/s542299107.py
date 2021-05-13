def main():
    N, C, K = map(int, input().split())
    T = list(int(input()) for _ in range(N))

    T.sort()

    ans = 0
    temp = T[0]
    cnt = 1

    for i in range(1,N):
        if temp + K < T[i] or C == cnt:
            ans += 1
            temp = T[i]
            cnt = 1
        else:
            cnt += 1

    ans += 1
    return (ans)

print(main())