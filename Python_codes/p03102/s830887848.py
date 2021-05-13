n, m, c = map(int, input().split())
B = list(map(int, input().strip().split()))
A = [list(map(int, input().strip().split())) for i in range(n)]

out = 0
for i in range(n):
    smpr = 0
    for j in range(m):
        smpr += A[i][j] * B[j]
    if smpr + c > 0:
        out += 1
print(out)