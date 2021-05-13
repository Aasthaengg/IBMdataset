def resolve():
    S = str(input())
    K = int(input())

    if S[0] != '1':
        print(S[0])
        return
    else:
        for i in range(1, K):
            if S[i] != '1':
                print(S[i])
                return
            else:
                continue
        print('1')

    return

resolve()