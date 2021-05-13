h, w, k = map(int, input().split())
dp = [1] + [0] * (w - 1)
mod = 1000000007

def mul(a, b):
    newmatrix = [[0] * w for _ in range(w)]
    for i in range(w):
        for j in range(w):
            newmatrix[i][j] = sum(a[i][k] * b[k][j] for k in range(w)) % mod
    return newmatrix

matrix = [[0] * w for _ in range(w)]
for b in range(1 << (w - 1)):
    valid = True
    for i in range(w - 1):
        if (b >> i) & 3 == 3:
            valid = False
    if valid:
        for i in range(w):
            if (b >> i) & 1 != 0:
                matrix[i][i + 1] += 1
            elif i > 0 and (b >> (i - 1)) & 1 != 0:
                matrix[i][i - 1] += 1
            else:
                matrix[i][i] += 1

ret = [[1 if i == j else 0 for i in range(w)] for j in range(w)]
while h > 0:
    if h & 1 == 1:
        ret = mul(ret, matrix)
    matrix = mul(matrix, matrix)
    h //= 2

print(ret[0][k - 1])
