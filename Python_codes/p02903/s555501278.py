h, w, a, b = map(int, input().split())
s = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if (i < b and j < a) or (b <= i and a <= j):
            s[i][j] = 1
for t in s:
    print("".join(map(str, t)))