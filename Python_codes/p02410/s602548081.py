A = []
b = []
output = []
n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
b = [int(input()) for j in range(m)]
output = [0 for p in range(n)]

for k in range(n):
    for l in range(m):
        output[k] += A[k][l] * b[l]

for o in range(n):
    print(output[o])