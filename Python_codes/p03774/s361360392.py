N,M = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(N)]

c =[[int(i) for i in input().split()] for j in range(M)]

n = 100000000000
n1 = 0
n2 = 0

for i in range(N):
    for j in range(M):
        n1 = abs(c[j][0] - a[i][0]) + abs(c[j][1] - a[i][1])
        if n1 < n:
            n = n1
            n2 = j
    n = 100000000000
    print(n2 + 1)
