def resolve():
    S = str(input())
    N = len(S)

    one = False
    pt = 0
    ans = 0

    while pt < N:
        if (pt == N - 2 and S[pt] == S[pt + 1]):
            ans += 1
            break

        if (one and S[pt] == S[pt - 1]):
            ans += 1
            pt += 2
            one = False
        else:
            ans += 1
            pt += 1
            one = True

    print(ans)

    return

resolve()