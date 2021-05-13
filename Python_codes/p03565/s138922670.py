S = input()[::-1]
T = input()[::-1]

p = 0
e = len(T)
ans = ''
while 1:
    s = S[p:e]

    if len(s) != len(T):
        print('UNRESTORABLE')
        break
    tmp = ''
    for i in range(len(T)):
        if s[i] == T[i] or s[i] == '?':
            tmp += T[i]
        else:
            ans += s[0]
            break
    else:
        ans += tmp
        ans += S[e::]
        print(ans.replace('?','a')[::-1])
        exit()
    p += 1
    e += 1