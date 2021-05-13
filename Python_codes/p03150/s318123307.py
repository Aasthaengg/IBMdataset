S = input()
key = 'keyence'
ok = False
for i in range(8):
    # print(S[i-8:i])
    if i == 7:
        j = S[:7]
    else:
        j = S[:i] + S[i-7:]
    if key == j:
        ok = True

if ok:
    print('YES')
else:
    print('NO')