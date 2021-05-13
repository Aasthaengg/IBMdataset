import sys
input = sys.stdin.readline

#input
N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

#output
C = [a+b for a, b in zip(A, B)]
C.sort(reverse = True)
accum = 0
for i in range(N):
    if i % 2 == 0:
        accum += C[i]
answer = accum - sum(B)
print(answer)
