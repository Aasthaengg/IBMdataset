S=input()
Q=[s for s in S if s != 'A']
U=list('KIHBR')
import sys
if S.count('A')>4:
    print('NO')
    sys.exit()
elif len(Q)!=5:
    print('NO')
    sys.exit()
for i in range(len(S)):
    if S[i] not in list('AKIHABARA'):
        print('NO')
        sys.exit()
for i in range(len(S)-1):
    if S[i]==S[i+1]:
        print('NO')
        sys.exit()
    elif S[i]=='K' and S[i+1]!='I':
        print('NO')
        sys.exit()
    elif S[i]=='I' and S[i+1]!='H':
        print('NO')
        sys.exit()
for i in range(len(U)):
    if Q[i]==U[i]:
        pass
    else:
        print('NO')
        break
else:
    print('YES')