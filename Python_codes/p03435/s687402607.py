import numpy as np
c1 = list(map(int,input().split()))
c2 = list(map(int,input().split()))
c3 = list(map(int,input().split()))
C = np.array([c1,c2,c3])
Ct = np.transpose(C)
ans = C + Ct
fact = "Yes"
for i in range(3):
    for j in range(3):
        if not(ans[i,j] == C[i,i] + C[j,j]):
            fact = "No"
            break
print(fact)
