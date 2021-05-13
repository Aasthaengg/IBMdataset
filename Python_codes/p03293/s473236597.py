def resolve():
    S = input().strip()
    T = input().strip()

    for i in range(len(S)):
        if S == T:
            print('Yes')
            return
        S = S[len(S) - 1] + S[0:len(S) - 1]
    if S == T:
        print('Yes')
    else:
        print('No')
resolve()
