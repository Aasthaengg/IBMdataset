s = list(input())
t = list(input())
ns = len(s)
nt = len(t)

flag = False
if ns < nt:
    print('UNRESTORABLE')
    exit()
for i in reversed(range(ns-nt+1)):
    for j in range(nt):
        if s[i:i+nt][j] != '?' and s[i:i+nt][j] != t[j]:
            break
    else:
        s[i:i+nt] = t
        flag = True
        break
if flag:
    ans = ''.join(s).replace('?', 'a')
    print(ans)
else:
    print('UNRESTORABLE')
