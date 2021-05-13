h, w, a, b = (int(x) for x in input().split())
S = [[""] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if (0 <= i < b and 0 <= j < a) or (b <= i < h and a <= j < w):
            S[i][j] = '1'
        else:
            S[i][j] = '0'

for ans in S:
    print("".join(ans))
