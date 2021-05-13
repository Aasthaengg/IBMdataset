def resolve():
    N = int(input())
    S = [int(i) for i in input().split()]
    int(input())
    T = [int(i) for i in input().split()]

    ans = 0
    # S.append(-1)
    for t in T:
        for s in S:
            if s == t:
                ans += 1
                break
        # i = 0
        # S[N] = t
        # while S[i] != t:
        #     i += 1
        # if i != N:
        #     ans += 1
    print(ans)


resolve()
