A, B = map(int, input().split())
A -= 1
B -= 1
G = []
for h in range(50):
    G.append(["#"]*100)
for h in range(50):
    G.append(["."]*100)
i, j = 0, 0
for _ in range(A):
    G[i][j] = "."
    j += 2
    if j>=100:
        i += 2
        j = 0
i, j = 99, 0
for _ in range(B):
    G[i][j] = "#"
    j += 2
    if j>=100:
        i -= 2
        j = 0
print(100,100)
for i in range(100):
    print("".join(G[i]))