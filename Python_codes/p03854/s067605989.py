S = input()

L = ['maerd', 'remaerd', 'esare', 'resare']
T = ''
for i in range(len(S) - 1, -1, -1):
    T += S[i]
    if T not in L and len(T) > 7:
        print('NO')
        exit()
    elif T in L:
        T = ''

print('YES')
