import itertools
n = int(input())
a = list(map(int,input().split()))
b = [[0] * 3 for i in range(n)]
for i in range(n):
    b[i][0] = a[i] - 1
    b[i][1] = a[i]
    b[i][2] = a[i] + 1
c = list(itertools.product(*b))
cnt = 0
for i in range(len(c)):
    x = c[i][0]
    for j in range(1, n):
        x = x * c[i][j]
    if x % 2 == 0:
        cnt += 1

print(cnt)