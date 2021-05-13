N = int(input())
C = [int(input()) for _ in range(N)]

mod = 10**9+7
newC = [C[0]]
for c in C:
    if newC[-1] == c:
        continue
    newC.append(c)

N = len(newC)
L = [0]*(N+1)
L[0] = 1
idx = [-1]*(max(newC)+1)
for i in range(N):
    if idx[newC[i]] >= 0:
        L[i+1] += L[idx[newC[i]]]
        
    L[i+1] += L[i]
    L[i+1] %= mod
    idx[newC[i]] = i+1

print(L[-1])