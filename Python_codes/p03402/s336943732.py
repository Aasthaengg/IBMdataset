a, b = map(int, input().split())
s = [[0 for _ in range(100)] for _ in range(100)]
for i in range(100):
    for j in range(100):
        if j == 0:
            s[i][j] = "."
        elif j == 99:
            s[i][j] = "#"
        else:
            if i % 2 == 0:
                s[i][j] = "#"
            else:
                s[i][j] = "."
c, d = 0, 2
while b != 1:
    s[c][d] = "."
    b -= 1
    d += 2
    if d > 95:
        c += 6
        d = 2
c, d = 3, 97
while a != 1:
    s[c][d] = "#"
    a -= 1
    d -= 2
    if d < 4:
        c += 6
        d = 97
print(100, 100)
for t in s:
    print("".join(t))