N, A, B, C, D = list(map(int, input().split()))
S = input()

A -= 1
B -= 1
C -= 1
D -= 1

right_end = max(C, D)
S = S[A:right_end+1]

ans = True
if A < B < C < D:
    if S.count('##'):
        ans = False
elif A < C < B < D:
    if S[A:C+1].count('##') or S[B:D+1].count('##'):
        ans = False
else:
    if S.count('##'):
        ans = False
    elif S[B:D+2].count('...'):
        pass
    elif S[B-1:B+2] == '...':
        pass
    else:
        ans = False

if ans:
    print('Yes')
else:
    print('No')

# print(S)
# print(iwaiwa)
# print(S[B-1:B+2])
