N = int(input())
A = [[],[]]
A[0] = [int(_) for _ in input().split()]
A[1] = [int(_) for _ in input().split()]

totals = []
for j in range(N):
    totals.append(sum(A[0][0:j+1]) + sum(A[1][j:]))

print(max(totals))