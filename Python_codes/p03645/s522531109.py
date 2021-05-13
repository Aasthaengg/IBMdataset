n, m = map(int, input().split())
x = [0]*n
y = [0]*n
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a == 0:
        x[b] = 1
    if b == n-1:
        y[a] = 1

f = 0
for i in range(n):
    if x[i]*y[i] > 0:
        f = 1

if f:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")