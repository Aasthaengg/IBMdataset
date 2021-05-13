import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = [[False, 0] for i in range(N)]
for i in range(M):
    p, S = input().split()
    p = int(p)
    if S == "WA":
        if not L[p - 1][0]:
            L[p-1][1] += 1
    elif S == "AC":
        if not L[p - 1][0]:
            L[p-1][0] = True

AC = 0
PN = 0
for i in range(N):
    if L[i][0]:
        AC += 1
        PN += L[i][1]
print(AC, PN)
