S = input()
N = len(S)

def check(S1):
    if S1 != S1[::-1]:
        return False
    else:
        return True

POS = int((N-1)/2)
S1 = S[0:POS]
POS = int((N+3)/2)
S2 = S[POS-1:N]

if check(S) == False or check(S1) == False or check(S2) == False:
    print('No')
else:
    print('Yes')

