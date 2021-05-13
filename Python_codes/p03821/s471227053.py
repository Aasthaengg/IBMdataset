N = int(input())
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ctr = 0

for i in reversed(range(N)):
    if (A[i] + ctr) % B[i] == 0: continue
    ctr += B[i] - ((A[i] + ctr) % B[i])

print(ctr)