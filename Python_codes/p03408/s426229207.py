N = int(input())
C = {}
for _ in range(N):
    a = input().strip()
    if a not in C:
        C[a] = 0
    C[a] += 1
M = int(input())
for _ in range(M):
    a = input().strip()
    if a not in C:
        C[a] = 0
    C[a] -= 1
cmax = -100
for a in C:
    cmax = max(cmax,C[a])
print(max(0,cmax))