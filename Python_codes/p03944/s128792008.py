W, H, N = map(int, input().split())
check = [list(map(int, input().split())) for i in range(N)]

rect = [["W" for i in range(W)] for j in range(H)]

for x in check:
    if x[2] == 1:
        for h1 in range(H):
            for w1 in range(x[0]):
                rect[h1][w1] = "B"

    elif x[2] == 2:
        for h2 in range(H):
            for w2 in range(x[0], W, 1):
                rect[h2][w2] = "B"
    elif x[2] == 3:
        for h3 in range(x[1]):
            for w3 in range(W):
                rect[h3][w3] = "B"

    elif x[2] == 4:
        for h3 in range(x[1], H, 1):
            for w3 in range(W):
                rect[h3][w3] = "B"


count = 0
for y in rect:
    count += y.count("W")
print(count)
