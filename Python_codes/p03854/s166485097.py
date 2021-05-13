S = list(input())
S.reverse()
S = ''.join(S)
idx = 0
len_S = len(S)
flag = True
while idx != len_S:
    if (len_S - idx > 6) and (S[idx:idx+7] == 'remaerd'):
        idx += 7
    elif (len_S - idx > 5) and (S[idx:idx+6] == 'resare'): 
        idx += 6
    elif (len_S - idx > 4) and (S[idx:idx+5] == 'maerd'): 
        idx += 5
    elif (len_S - idx > 4) and (S[idx:idx+5] == 'esare'): 
        idx += 5
    else:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')
