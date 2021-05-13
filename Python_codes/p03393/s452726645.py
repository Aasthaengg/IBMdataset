S = list(input())

if len(S) < 26:
    W = list('abcdefghijklmnopqrstuvwxyz')
    for s in S:
        W.remove(s)
    S += W[0]
    print(*S, sep='')
else:
    s_last = S[-1]
    idx = -1
    for i in range(24, -1, -1):
        s = S[i]
        if s > s_last:
            s_last = s
        else:
            idx = i
            break
    if idx == -1:
        print(-1)
    else:
        res = []
        for s in S[idx+1:]:
            if s > S[idx]:
                res.append(s)
        res.sort()
        print(*(S[:idx] + [res[0]]), sep='')
