N = int(input())
A = list(map(int,input().split()))

S = sum(A)
chk = 0
i = 2
while i < N:
    chk += A[i-1]
    i += 2
chk *= 2
M = [0] * N

#print(chk,S)
M[0] = S - chk

for i in range(1,N):
    M[i] = 2 * A[i-1] - M[i-1]
print(*M)