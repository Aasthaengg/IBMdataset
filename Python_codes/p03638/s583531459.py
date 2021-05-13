H, W = map(int, input().split())
N = int(input())
cells = []
for idx, a in enumerate(map(int, input().split())):
    cells.extend([idx + 1 for _ in range(a)])

for i in range(H):
    if i % 2 == 0:
        print(*cells[i*W:(i+1)*W])
    else:
        print(*cells[i*W:(i+1)*W][::-1])
