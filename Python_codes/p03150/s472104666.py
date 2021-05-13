S = input()
if S == 'keyence':
    print('YES')
    exit()

for i in range(1,len(S)-7+1):
    for j in range(len(S)):
        ns = S[:j]+S[j+i:]
        if ns == 'keyence':
            print('YES')
            exit()
print('NO')
