N = int(input())
D, X = list(map(int, input().split()))
A = []
for _ in range(N):
    A += [int(input())]

ate_amount = []
for i in range(N):
    ate_amount += [int((D - 1) // A[i]) + 1]

print(X + sum(ate_amount))