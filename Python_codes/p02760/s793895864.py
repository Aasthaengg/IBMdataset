Aij = []
c = 0
for i in range(3):
    Aij += list(map(int, input().split()))
    
N = int(input())
for i in range(N):
    b = int(input())
    if b in Aij:
        Aij[Aij.index(b)] = 0

for i in range(3):
    if Aij[3*i] == Aij[3*i+1] and Aij[3*i] == Aij[3*i+2]:
        c = -1
        break

    if Aij[i] == Aij[i+3] and Aij[i] == Aij[i+6]:
        c = -1
        break

if c == Aij[4]:
    if Aij[0] == Aij[4] and Aij[4] == Aij[8]:
        c = -1
    elif Aij[2] == Aij[4] and Aij[4] == Aij[6]:
        c = -1
    else:
        pass

print(['No', 'Yes'][c])