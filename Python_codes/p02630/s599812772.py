# input
N = int(input())
L = [0] * 100001
A = list(map(int, input().split()))
for i in A: L[i] += 1
Q = int(input())
S = sum(A)
for i in range(Q):
    B, C = map(int, input().split())
    S += L[B] * (C - B)
    L[C] += L[B]
    L[B] = 0
    print(S)

