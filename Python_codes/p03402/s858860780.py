from itertools import product

A, B = map(int, input().split())
A -= 1
B -= 1

G = [["#" for _ in range(100)] for _ in range(50)]
for i, j in product(range(0, 50, 2), repeat=2):
    if A <= 0:
        break
    G[i][j] = "."
    A -= 1

H = [["." for _ in range(100)] for _ in range(50)]
for i, j in product(range(1, 51, 2), repeat=2):
    if B <= 0:
        break
    H[i][j] = "#"
    B -= 1

print(100, 100)
for g in G:
    print("".join(g))

for h in H:
    print("".join(h))
