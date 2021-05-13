h, w = (int(x) for x in input().split())
S = [list(input()) for _ in range(h)]

next_x = [1, 0, -1, 0]
next_y = [0, 1, 0, -1]

for y in range(h):
    for x in range(w):
        if S[y][x] == "#":
            for i in range(4):
                nx = x + next_x[i]
                ny = y + next_y[i]
                if 0 <= nx < w and 0 <= ny < h and S[ny][nx] == "#":
                    break
            else:
                print("No")
                exit()

print("Yes")
