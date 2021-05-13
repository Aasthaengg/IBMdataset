def resolve():
    S = str(input())
    if S[3 - 1] == S[4 - 1] and S[5 - 1] == S[6 - 1]:
        print('Yes')
        return
    print('No')
    return

resolve()