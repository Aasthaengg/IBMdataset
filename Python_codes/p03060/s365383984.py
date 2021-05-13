N = int(input())
V = [int(n) for n in input().split()]
C = [int(n) for n in input().split()]

profit = 0
for i in range(N):
    if V[i] - C[i] >= 0:
        profit += V[i] - C[i]

print(profit)