H, W = map(int, input().split())
C = [None] * H
for i in range(H):
    C[i] = input()

for i in range(2 * H):
    print(C[int(i / 2)])
