N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

A = sorted(A)
B = sorted(B)
C = sorted(C)

BB = [0] * N

cidx = 0
for i in range(N):
    while cidx < N and C[cidx] <= B[i]:
        cidx += 1
    BB[i] = N - cidx

BBB = [0] * N
for i in range(N - 1, -1, -1):
    if (i == N - 1):
        BBB[i] = BB[i]
    else:
        BBB[i] = BB[i] + BBB[i+1]

sum = 0
bidx = 0
for i in range(N):
    while bidx < N and B[bidx] <= A[i]:
        bidx += 1
    if bidx != N:
        sum += BBB[bidx]

print(sum)
