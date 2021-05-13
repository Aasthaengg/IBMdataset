S = input()

while len(S) != 0:
    if S[-2:] == 'er':
        S = S[:-2]
        if S[-5:] == 'dream':
            S = S[:-5]
        elif S[-4:] == 'eras':
            S = S[:-4]
        else:
            print('NO')
            exit()
    else:
        if S[-5:] == 'dream' or S[-5:] == 'erase':
            S = S[:-5]
        else:
            print('NO')
            exit()

print('YES')