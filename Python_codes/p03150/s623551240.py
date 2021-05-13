S = input()

k = 'keyence'
if S[:7] == k or S[-7:] == k:
    print('YES')
    exit()
for i in range(len(S)):
    if S[:i] != k[:i]:
        if S[-7+i-1:] == k[-7+i-1:]:
            print('YES')
            exit()
        else:
            print('NO')
            exit()
print('NO')