S = list(input())
T = list(input())
s_appeared = [0] * 26
t_appeared = [0] * 26
for i in range(len(S)):
    if S[i] != T[i]:
        s_temp = s_appeared[ord(S[i])-97]
        if s_temp == 0:
            s_appeared[ord(S[i])-97] = T[i]
        else:
            if T[i] != s_temp:
                print('No')
                break

        t_temp = t_appeared[ord(T[i])-97]
        if t_temp == 0:
            t_appeared[ord(T[i])-97] = S[i]
        else:
            if S[i] != t_temp:
                print('No')
                break
    else:
        s_appeared[ord(S[i])-97] = T[i]
        t_appeared[ord(T[i])-97] = S[i]
else:
    print('Yes')