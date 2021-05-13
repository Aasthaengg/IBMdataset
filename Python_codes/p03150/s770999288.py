S = input()

for i in range(len(S)-1):
    for j in range(i,len(S)):
        memo = S[:i]+S[j:]
        #print(memo)
        if memo == 'keyence':
            print('YES')
            exit()
print('NO')