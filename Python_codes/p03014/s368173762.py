H, W = map(int, input().split())
Ss = [input() for _ in range(H)]

# 各マスから左に何マスいったら壁にぶつかるか
left = [[-1 for _ in range(W)] for _ in range(H)]
right = [[-1 for _ in range(W)] for _ in range(H)]
top = [[-1 for _ in range(W)] for _ in range(H)]
bottom = [[-1 for _ in range(W)] for _ in range(H)]


# 左に何マスいったらぶつかるか
for i in range(H):
    count = 0
    for j in range(W):
        if Ss[i][j] == "#":
            count = 0
        else:
            left[i][j] = count
            count += 1

# 右に何マスいったらぶつかるか
for i in range(H):
    count = 0
    for j in range(W):
        k = W-j-1
        if Ss[i][k] == "#":
            count = 0
        else:
            right[i][k] = count
            count += 1

# 上に何マスいったらぶつかるか
for j in range(W):
    count = 0
    for i in range(H):
        if Ss[i][j] == "#":
            count = 0
        else:
            top[i][j] = count
            count += 1

# 下に何マスいったらぶつかるか
for j in range(W):
    count = 0
    for i in range(H):
        k = H - i - 1
        if Ss[k][j] == "#":
            count = 0
        else:
            bottom[k][j] = count
            count += 1

# print("right")
# for i in range(H):
#     print(right[i])
#
# print("left")
# for i in range(H):
#     print(left[i])
#
# print("bottom")
# for i in range(H):
#     print(bottom[i])
#
# print("top")
# for i in range(H):
#     print(top[i])

max_score = 0
for i in range(H):
    for j in range(W):
        if Ss[i][j] != "#":
            score = left[i][j] + right[i][j] + top[i][j] + bottom[i][j] + 1
            max_score = max(max_score, score)

print(max_score)
