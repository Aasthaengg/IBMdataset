A, B, C = map(int,input().split())

if A == 1 and B == 1 and C == 1:
    print(0)
    exit()

elif A == B == C:
    print(-1)
    exit()

LA = []
LB = []
LC = []
LA.append(A)
LB.append(B)
LC.append(C)
i = 0
cnt = 0

while LA[i] % 2 == 0 and LB[i] % 2 == 0 and LC[i] % 2 == 0:
    LA.append((LB[i]+LC[i])/2)
    LB.append((LC[i]+LA[i])/2)
    LC.append((LA[i]+LB[i])/2)
    i += 1
    cnt += 1

print(cnt)