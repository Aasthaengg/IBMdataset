import sys
A, B = map(int,input().split())
S = input()
for i in range(A + B + 1):
    if i == A:
        if S[i] != '-':
            print('No')
            sys.exit()
    else:
        if not S[i] in '0123456789':
            print('No')
            sys.exit()
print('Yes')