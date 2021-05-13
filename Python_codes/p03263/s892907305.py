H, W = map(int, input().split())
A = []
total = 0
for _ in range(H):
    row = list(map(int, input().split()))
    A.append(row)
    total += sum(row)

lines = []
for y in range(H - 1):
    for x in range(W):
        if A[y][x] % 2 == 1:
            lines.append(f'{y+1} {x+1} {y+2} {x+1}')
            A[y][x] -= 1
            A[y + 1][x] += 1
y = H - 1
for x in range(W - 1):
    if A[H - 1][x] % 2 == 1:
        lines.append(f'{y+1} {x+1} {y+1} {x+2}')
        A[y][x] -= 1
        A[y][x + 1] += 1
print(len(lines))
for line in lines:
    print(line)