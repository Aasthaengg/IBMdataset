N, A, B, C, D = map(int, input().split())
S = input()
for i in range(A-1,max(C,D)-1):
    if S[i] == '#' and S[i+1] == '#':
        print('No')
        exit()
if D < C:
    for i in range(B-2,N-2):
        if S[i] == '.' and S[i+1] == '.' and S[i+2] == '.':
            print('Yes')
            exit()
        if i+1 == D-1:
            break
    print('No')
    exit()
else:
    print('Yes')
    exit()