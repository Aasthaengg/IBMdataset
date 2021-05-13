O = list(input())
E = list(input())
S = []
N1 = len(E)
N2 = len(O)
for i in range(N1):
    S.append(O[i])
    S.append(E[i])
if N1 < N2:
    S.append(O[-1])
print(''.join(S))