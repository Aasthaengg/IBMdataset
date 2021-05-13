h, w = [int(i) for i in input().split()]
paint = [list(input()) for j in range(h)]
ans = "Yes"

for i in range(h):
    for j in range(w):

        if paint[i][j] == "#":
            left = paint[i][j-1] == "#" if j > 0 else False
            right = paint[i][j+1] == "#" if j < w-1 else False
            top = paint[i-1][j] == "#" if i > 0 else False
            bottom = paint[i+1][j] == "#" if i < h-1 else False

            if not any([left, right, top, bottom]):
                ans = "No"
                break
    if ans == "No":
        break

print(ans)
