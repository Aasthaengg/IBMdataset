from collections import Counter
N = int(input())
A = input()
B = input()
C = input()

ans = 0
for i in range(N):
    naga = len(set([A[i],B[i],C[i]]))
    if naga == 3:
        ans+=2
    if naga == 2:
        ans+=1
print(ans)