N = int(input())
A = list(map(int, input().split()))
Q = int(input())

t = [0] * 110000

for i in range(N):
    a = A[i]
    t[a] += 1

a = sum(A)

B = [0] * Q
C = [0] * Q
for i in range(Q):
    B[i], C[i] = map(int, input().split())

for i in range(Q):
    a = a + (C[i] - B[i]) * t[B[i]]
    t[C[i]] = t[C[i]] + t[B[i]]
    t[B[i]] = 0
    print(a)