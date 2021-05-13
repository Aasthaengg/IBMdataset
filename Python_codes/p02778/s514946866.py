s = str(input())
S = list(s)
for i in range(len(S)):
    S.append('x')
    S.pop(0)
print(''.join(S))