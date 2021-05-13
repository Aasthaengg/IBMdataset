#B - AcCepted
S = list(input())
judge = 0
if S[0].isupper() == True:
    judge += 1
if 'C' in S[2:-1] and S.count('C') == 1:
    judge += 1
if 'C' in S:
    S.remove('C')
if 'A' in S:
    S.remove('A')
if all(S[i].islower() for i in range(len(S))) == True:
    judge += 1
if judge == 3:
    print('AC')
else:
    print('WA')