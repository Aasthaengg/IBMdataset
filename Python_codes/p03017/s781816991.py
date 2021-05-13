N, A, B, C, D = map(int, input().split())
S = '$' + input() + '$'

def isOk(fr, to):
    if S[fr: to + 1].count('##') > 0:
        return False
    return True

if not (isOk(A, C) and isOk(C, D)):
    print('No')
    exit()

def canSwitch():
    if A + 1 == B and D < C and S[A: A + 3] == '...':
        return True
    if B + 1 == A and C < D and S[B: B + 3] == '...':
        return True
    if C + 1 == D and B < A and S[C - 1: D + 1] == '...':
        return True
    if D + 1 == C and A < B and S[D - 1: C + 1] == '...':
        return True
    if A < B and S[B - 1: B + 2] == '...':
        return True
    if B < A and S[A - 1: A + 2] == '...':
        return True
    if C < D and S[C - 1: C + 2] == '...':
        return True
    if D < C and S[D - 1: D + 2] == '...':
        return True
    if S[max(A, B): min(C, D) + 1].count('...'):
        return True
    return False

if A < B and D < C or B < A and C < D:
    if not canSwitch():
        print('No')
        exit()

print('Yes')
