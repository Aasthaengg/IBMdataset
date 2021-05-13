S=input()
n=len(S)
for i in range(8):
    if S[:i]+S[n-7+i:]=='keyence':
        print('YES')
        exit()
print('NO')