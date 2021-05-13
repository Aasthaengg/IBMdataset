import sys
input = sys.stdin.readline


n, m = map(int, input().split())

A = []
for i in range(m):
    p, y = map(int, input().split())
    A.append([p, y, i])
A.sort()

x = 1
A[0].append(x)
for i in range(1, m):
    if A[i][0] == A[i - 1][0]:
        x += 1
    else:
        x = 1
    A[i].append(x)
A.sort(key = lambda x: x[2])

for a in A:
    p, x = a[0], a[3]
    print(format(p, "06") + format(x, "06"))
