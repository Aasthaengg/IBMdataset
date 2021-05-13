def match_len(S, T):
    ls, lt = len(S), len(T)
    ret = 0
    for i in range(ls - lt + 1):
        tmp = 0
        for x, y in zip(S[i:], T):
            tmp += x == y
        ret = tmp if tmp > ret else ret
    return ret

S = input()
T = input()
print(len(T) - match_len(S, T))