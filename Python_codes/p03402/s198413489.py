A, B = map(int, input().split())
m = [["."] * 100 for _ in range(50)]


def fill(f, b, i, j, n):
    for k in range(5):
        for l in range(5):
            m[i + k][j + l] = b
    m[i + 1][j + 1] = f if n > 0 else b
    m[i + 1][j + 3] = f if n > 1 else b
    m[i + 2][j + 2] = f if n > 2 else b
    m[i + 3][j + 1] = f if n > 3 else b
    m[i + 3][j + 3] = f if n > 4 else b


A -= 1
B -= 1
for i in range(0, 25, 5):
    for j in range(0, 100, 5):
        n = min(5, A)
        A -= n
        fill(".", "#", i, j, n)
for i in range(25, 50, 5):
    for j in range(0, 100, 5):
        n = min(5, B)
        B -= n
        fill("#", ".", i, j, n)

print(50, 100)
for v in m:
    print("".join(v))
