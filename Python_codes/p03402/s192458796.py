W, B = map(int, input().split())
h = 100
w = 100
X = [['#'] * w if i < (h // 2) else ['.'] * w for i in range(h)]

for i in range(0, h, 2):
    for j in range(0, w, 2):
        if W == 1:
            break
        X[i][j] = '.'
        W -= 1

for i in range(h//2 + 1, h, 2):
    for j in range(0, w, 2):
        if B == 1:
            break
        X[i][j] = '#'
        B -= 1
print(h, w)
for i in range(h):
    print("".join(X[i]))