n, m = map(int, input().split())
A = [[0 for i in range(m)] for j in range(n)]
b = [0 for i in range(m)]
c = [0 for i in range(n)]

i = 0
while i < n:
    l = list(map(int, input().split()))
    A[i] = l
    i += 1

i = 0
while i < m:
    l = int(input())
    b[i] = l
    i += 1

i = 0
j = 0
while i < n:
    while j < m:
        c[i] += A[i][j] * b[j]
        j += 1
    i += 1
    j = 0

for i in c:
    print(i)