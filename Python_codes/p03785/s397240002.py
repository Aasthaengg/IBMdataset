def solve():

    N, C, K = map(int, input().split())
    T = [int(input()) for i in range(N)]

    T = sorted(T)
    i = 0
    k = 0

    ans = 0

    #print(T)

    while i < N:
        n = 0
        while k < N and n < C and T[i] <= T[k] <= T[i]+K:
            n += 1
            k += 1
            if n == C:
                ans += 1
                break

        if n != C:
            ans += 1

        i = k



    print(ans)            


if __name__ == "__main__":
    solve()
