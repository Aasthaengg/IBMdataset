N,M,Q = map(int,input().split())
A = [0]*Q
B = [0]*Q
C = [0]*Q
D = [0]*Q
for i in range(Q):
    A[i],B[i],C[i],D[i] = map(int,input().split())

from itertools import combinations_with_replacement as comb_rplc
answer = 0

for seq in comb_rplc(range(1,M+1),N):
    candi = 0
    
    for i in range(Q):
        if seq[B[i]-1]-seq[A[i]-1] == C[i]:
            candi += D[i]
    answer = max(candi,answer)
print(answer)