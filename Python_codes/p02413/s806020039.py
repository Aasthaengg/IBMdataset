r, c = map(int, input().split())

a = [[0 for j in range(c)] for i in range(r)]
for i in range(r):
    a[i] = list(map(int, input().split()))

rsum = [0 for i in range(r)]
csum = [0 for i in range(c)]
for i in range(r):
    rsum[i] = sum(a[i])
    for j in range(c):
        csum[j] += a[i][j]
allsum = sum(rsum)

for i in range(r):
    for j in range(c):
        print(a[i][j], end = " ")
    print(rsum[i])
for i in range(c):
    print(csum[i], end = " ")
print(allsum)