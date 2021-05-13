N = int(input())
A = [int(a) for a in input().split()]

M = 10**6
P = [0]*(M+1)
for i in range(2, M+1):
    if P[i] == 1:
        continue
    P[i] = -1
    j = 2*i
    while j <= M:
        P[j] = 1
        j += i

L = [0]*(M+1)
for a in A:
    L[a] += 1

num = 0
for i in range(2, M+1):
    if P[i] > -1:
        continue
    cnt = 0
    j = i
    while j <= M:
        cnt += L[j]
        j += i
    num = max(num, cnt)


if num == 1 or max(A) == 1:
    print("pairwise coprime")
elif num == N:
    print("not coprime")
else:
    print("setwise coprime")