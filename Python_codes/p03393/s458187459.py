def check():
    S = input()
    s_set = set(S)
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    if len(S) == 26:
        if S == alpha[::-1]:
            return -1
        else:
            for i in range(1,len(S)+1):
                S1 = S[-i:]
                if S1 != ''.join(sorted(S1, reverse=True)):
                    S1 = S1[1:]
                    break
            for s in S1[::-1]:
                if s > S[-i]:
                    return S[:-i]+s
    else:
        for a in alpha:
            if a not in s_set:
                return S+a
print(check())