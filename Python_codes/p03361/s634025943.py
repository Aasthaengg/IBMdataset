# input
H, W = map(int, input().split())
s = [
    list(input())
    for i in range(H)
]

# check
for i in range(H):
    for j in range(W):
        if s[i][j] == ".":
            continue
        else:
            check = []
            append = check.append

            if i - 1 >= 0:
                append(s[i - 1][j])
            if i + 1 < H:
                append(s[i + 1][j])
            if j - 1 >= 0:
                append(s[i][j - 1])
            if j + 1 < W:
                append(s[i][j + 1])

            if set(check) == {"."}:
                print("No")
                exit(0)
print("Yes")