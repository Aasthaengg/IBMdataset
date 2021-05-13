S = input()
flag = False
if S.count('keyence') > 0:
    flag = True
else:
    key = 'keyence'
    i = 0
    while key[i] == S[i]:
        i += 1
    if key[i:] == S[-(7-i):]:
        flag = True
print('YES' if flag else 'NO')
