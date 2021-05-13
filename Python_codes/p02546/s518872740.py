S = list(input())
num = len(S) - 1
if S[num] == 's':
    S.append('e')
    S.append('s')
else:
    S.append('s')
print(''.join(S))