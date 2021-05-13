N = int(input())
l = []
for _ in range(N):
    A, B = map(int, input().split())
    l.append((-abs(A+B), -A, -B))
l.sort()
a, b = 0, 0
for i in range(N):
    if i%2:
        b -= l[i][2]
    else:
        a -= l[i][1]

print(a-b)
