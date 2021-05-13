S = input()
L = len(S)

if(S == 'keyence'):
    print('YES')
    exit()

for i in range(L):
    count = 0
    for j in range(i, L):
        if (i == 0 and count == 0):
            s = S[1:]
        elif(i == L - 1):
            s = S[:i]
        else:
            s = S[:i] + S[i + count + 1:]

        if (s == 'keyence'):
            print('YES')
            exit()
        else:
            count += 1

print('NO')
