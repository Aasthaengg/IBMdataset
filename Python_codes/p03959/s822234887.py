def inpl(): return list(map(int, input().split()))

N = int(input())
T = inpl()
A = inpl()

OK = True
D = [0]*N
D[0] = 1

for i in range(1, N):
    if T[i-1] < T[i]:
        D[i] = 1

if D[-1] and (A[-1] != T[-1]):
    OK = False
else:
    D[-1] = 1

for i in range(N-2, -1, -1):
    if A[i] > A[i+1]:
        if D[i] and (A[i] != T[i]):
            OK = False
        else:
            if A[i] > T[i]:
                OK = False
            D[i] = 1

ans = OK
MOD = 10**9 + 7
for i in range(N):
    if D[i] == 0:
        ans = ans * min(A[i], T[i]) % MOD
print(ans*1)