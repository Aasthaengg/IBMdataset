def main():
    N = int(input())
    S = list(input())

    CW = [0 for i in range(N + 1)]
    CE = [0 for i in range(N + 1)]

    count_w = count_e = 0

    for i in range(N):
        if S[i] == "W":
            count_w += 1
        CW[i + 1] = count_w

    S.reverse()
    
    for i in range(N):
        if S[i] == "E":
            count_e += 1
        CE[i + 1] = count_e

    S.reverse()

    ans = 10**6
    for i in range(N):
        w = CW[i] - CW[0]
        e = CE[N - (i + 1)] - CE[0]
        change = w + e

        if ans > change:
            ans = change

    print(ans)

if __name__ == "__main__":
    main()