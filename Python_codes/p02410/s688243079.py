s = input().split(" ")
n = int(s[0])
m = int(s[1])
a = [["" for i in range(m)]for j in range(n)]
b = []
c = []
for i in range(n):
    s = input().split(" ")
    for j in range(m):
        a[i][j] = int(s[j])
for i in range(m):
    b.append(int(input()))
for i in range(n):
    seki = 0
    for j in range(m):
        seki += a[i][j] * b[j]
    c.append(seki)
for i in range(n):
    print(c[i])