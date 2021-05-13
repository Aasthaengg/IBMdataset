N, M, C = input().split()
N = int(N)
M = int(M)
C = int(C)

B = []
b = list(map(int, input().split()))

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

results = [[sum(a*b for a,b in zip(x_row, b))] for x_row in A]

working = 0
for result in results:
    if ((result[0] + C) > 0):
        working += 1

print(working)