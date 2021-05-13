N = int(input())

div = 1
pairs = [[0] * 10 for i in range(10)]

for i in range(1,N+1):
    if i // div >= 10:
        div *= 10
        f = 1
    else:
        f = i//div
    pairs[f][i%10] += 1

res = 0
for i in range(1, 10):
    for j in range(1, 10):
        res += pairs[i][j] * pairs[j][i]
print(res)