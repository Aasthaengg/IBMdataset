def resolve():
    S = str(input())
    T = str(input())
    cnt = 0
    while True:
        S = S[-1] + S[:-1]
        cnt += 1
        if S == T:
            print('Yes')
            break
        if cnt > len(S):
            print('No')
            break
    return
resolve()