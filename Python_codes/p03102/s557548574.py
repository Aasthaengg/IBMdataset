n,m,c = map(int, input().split())
b = list(map(int, input().split()))
a = []
for i in range(n):
    am = list(map(int, input().split()))
    a.append(am)
num = 0
for h in range(n):
    t = 0
    for j in range(m):
        t += a[h][j]*b[j]
    if 0 < t+c:
        num += 1
print(num)