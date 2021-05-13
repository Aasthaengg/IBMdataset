N = int(input())
D, X = map(int, input().split())

A = [int(input()) for i in range(N)]

eated = 0

for i in range(len(A)):
    if A[i] == 1:
        eated += D
    elif D % A[i] == 0:
        eated += D // A[i]
    else:
        eated += D // A[i] + 1

print(X + eated)