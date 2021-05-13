N, A, B, C, D = list(map(int,input().split()))
S = input()

for i in range(A-1,C):
    if S[i] == '#' and S[i+1] == '#':
        print('No')
        exit()

for ii in range(B-1,D):
    if S[ii] == '#' and S[ii+1] == '#':
        print('No')
        exit()

if C > D:
    for j in range(B-1,D):
        if S[j-1] == '.' and S[j] == '.' and S[j+1] == '.':
            print('Yes')
            exit()

    print('No')
    exit()

else:
    print('Yes')
    exit()