H, W = map(int, input().split())
lines = [input() for i in range(H)]

for i in range(W + 2):
    print("#", end="")
print("")

for i in range(H):
    print("#", end="")
    print(lines[i], end="")
    print("#")

for i in range(W + 2):
    print("#", end="")
print("")
