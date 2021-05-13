S = input()
T = input()
s = len(S)
t = len(T)
for i in range(s - t, -1, -1):
    SS = S[i : i + t]
    for j in range(t):
        if SS[j] != '?' and SS[j] != T[j]:
            break
    else:   # 見つかった
        ans = S.replace('?', 'a')
        ans = ans[0 : i] + T + ans[i + t :]
        break
else:   # なかった
    ans = 'UNRESTORABLE'

print(ans)