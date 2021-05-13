import sys
S = input()
T = input()
if S == T:
    print('Yes')
else:
    num = len(S)
    for i in range(num):
        S = S[-1] + S[:-1]
        if S == T:
            print('Yes')
            sys.exit()
    print('No')
