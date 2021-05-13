N = int(input())
A = []
for i in range(2):
    A.append([int(a) for a in input().split()])

K = [sum(A[0][:n + 1]) + sum(A[1][n:]) for n in range(N)]
print(max(K))
