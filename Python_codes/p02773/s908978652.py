N = int(input())
C = {}
for _ in range(N):
    s = input().strip()
    if s not in C:
        C[s]=0
    C[s] += 1
cmax = 0
for s in C:
    cmax = max(cmax,C[s])
A = []
for s in C:
    if C[s]==cmax:
        A.append(s)
A = sorted(A)
for i in range(len(A)):
    print(A[i])