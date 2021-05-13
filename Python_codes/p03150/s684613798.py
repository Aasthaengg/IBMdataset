S = input()

s = 'keyence'
for i in range(1,len(S)):
    if S[:i] + S[i-7:] == s:
        print('YES')
        break
else:
    print('NO')