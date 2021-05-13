N = int(input())
T = [int(t) for t in input().split()]
A = [int(a) for a in input().split()]

mod = 10**9+7
TM = [0]*N
TM[0] = T[0]
AM = [0]*N
AM[-1] = A[-1]
for i in range(N-1):
    if T[i] < T[i+1]:
        TM[i+1] = T[i+1]
    if A[i+1] < A[i]:
        AM[i] = A[i]

M = [0]*N
ans = 1
for i in range(N):
    if TM[i] > 0 and AM[i] > 0 and TM[i] != AM[i]:
        ans = 0
    elif TM[i] > 0 and AM[i] == 0 and TM[i] <= A[i]:
        M[i] = TM[i]
    elif TM[i] == 0 and AM[i] > 0 and AM[i] <= T[i]:
        M[i] = AM[i]
    elif TM[i] == AM[i]:
        M[i] = TM[i]
    elif TM[i] == 0 and AM[i] == 0:
        continue
    else:
        ans = 0
        break

for i in range(N):
    if M[i] > 0:
        continue
    ans *= min(T[i], A[i])
    ans %= mod

print(ans)