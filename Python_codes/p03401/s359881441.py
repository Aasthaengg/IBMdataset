N = int(input())
A = [int(x) for x in input().split()]
A = [0] + A + [0]

S = 0
for i in range(len(A) - 1):
    S += abs(A[i] - A[i+1])
for i in range(1, len(A)-1):
    reg = S - abs(A[i-1] - A[i]) - abs(A[i] - A[i+1]) + abs(A[i-1] - A[i+1])
    print(reg)