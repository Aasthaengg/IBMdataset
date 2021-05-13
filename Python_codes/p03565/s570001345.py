S = input()
T = input()
ls = len(S)
lt = len(T)

S = S[::-1]
T = T[::-1]

ans = 'UNRESTORABLE'

if ls < lt:
    print(ans)
    exit()

i = 0
while i < ls - lt + 1:
    tmp = ''
    for j in range(lt):
        if S[i + j] == T[j] or S[i + j] == '?':
            tmp += S[i + j]
        else:
            break
    if len(tmp) == lt:
        ans = S.replace(tmp, T, 1)
        ans = ans.replace('?', 'a')
        print(ans[::-1])
        exit()
    i += 1

print(ans)
