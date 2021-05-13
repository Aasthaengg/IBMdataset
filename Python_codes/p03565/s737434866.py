S = input()
T = input()

s = len(S)
t = len(T)

ans = []
for i in range(s - t + 1):
    flg = 0
    for j in range(t):
        if S[i+j] == T[j]:
            pass
        elif S[i+j] == '?':
            pass
        else:
            flg = 1
            break
    if flg == 0:
        ans.append(S[0:i].replace('?', 'a') + T + S[i+t:].replace('?', 'a'))
if len(ans) == 0:
    print('UNRESTORABLE')
else:
    print(sorted(ans)[0])
