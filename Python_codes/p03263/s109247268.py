H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
output = []
for i in range(H-1):
    for j in range(W):
        if a[i][j] % 2 == 1:
            a[i+1][j] += 1
            output.append((i+1, j+1, i+2, j+1))

for i in range(W-1):
    if a[-1][i] % 2 == 1:
        a[-1][i+1] += 1
        output.append((H, i+1, H, i+2))
print(len(output))
for y, x, ay, ax in output:
    print(y, x, ay, ax)