#その10

O = str(input())
E = str(input())
P = []
for i in range(len(O)):
    P.append(O[i])
    if i < len(E):
        P.append(E[i])
print(''.join(P))