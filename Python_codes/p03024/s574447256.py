S = input()

batsu = 0
for i in range(len(S)):
    if S[i] == 'x':
        batsu += 1

if batsu >= 8:
    print('NO')
else:
    print('YES')
