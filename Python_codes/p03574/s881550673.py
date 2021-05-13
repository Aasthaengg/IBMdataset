# coding: utf-8

H, W = map(int, input().split(" "))

S = []
for i in range(H):
    tmp = input()
    S.append(list(tmp))


def eight_math_index(i, j, H, W):
    result = [(i-1, j-1), (i-1, j), (i-1, j+1),
              (i, j - 1), (i, j), (i, j + 1),
              (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
    return list(filter(lambda x: (0 <= x[0] <= (H-1)) and (0 <= x[1] <= (W-1)), result))


for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            eight = eight_math_index(i, j, H, W)
            S[i][j] = 0
            for (k, l) in eight:
                if S[k][l] == "#":
                    S[i][j] += 1

for l in S:
    print("".join(list(map(str, l))))


