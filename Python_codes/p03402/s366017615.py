A, B = map(int, input().split())

G = [["."] * 100 for i in range(50)] + [["#"] * 100 for i in range(50)]

A, B = A - 1, B - 1

for h in range(0, 50, 2):
    for w in range(0, 100, 2):
        if B != 0:
            G[h][w] = "#"
            B -= 1

for h in range(51, 100, 2):
    for w in range(0, 100, 2):
        if A != 0:
            G[h][w] = "."
            A -= 1

print(100, 100)
for g in G:
    print("".join(g))
