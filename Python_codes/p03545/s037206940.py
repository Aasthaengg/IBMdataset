S = [a for a in input()]
N = [int(a) for a in S]
M = [N[0]] + [-N[i] for i in range(1,4)]

S.insert(1, '+')
S.insert(3, '+')
S.insert(5, '+')

if sum(N) == 7:
    S = S
    print(''.join(S) + '=7')
    exit()

for i in range(1, 4):
    N[i] = -N[i]
    
    if sum(N) == 7:
        
        S[2 * i - 1] = '-'
        print(''.join(S) + '=7')
        exit()
    else: N[i] = -N[i]

for i in range(1, 4):
    S[1], S[3], S[5] = '-', '-', '-'
    
    M[i] = -M[i]
    
    if sum(M) == 7:
        S[2 * i - 1] = '+'
        print(''.join(S) + '=7')
        exit()
    else:
      M[i] = -M[i]