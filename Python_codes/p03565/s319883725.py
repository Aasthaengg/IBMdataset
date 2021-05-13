S = input()
T = input()
l = len(S)
lt = len(T)
ok = False
if l >= lt:
    for i in range(l - lt, -1, -1):
        SS = S[i:i+lt]
        can_replace = True
        for j, ss in enumerate(SS):
            can_replace *= (SS[j] == T[j] or SS[j] == '?')
        if can_replace:
            ok = True
            t_i = i
            break
if ok:
    S = S.replace('?', 'a')
    print(S[:t_i] + T + S[t_i + lt:])
else:
    print('UNRESTORABLE')