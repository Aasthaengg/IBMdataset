# coding: utf-8

H, W = map(int, input().split(" "))

S = []
for i in range(H):
    tmp = input()
    S.append(list(tmp))


def eight_math_index(i, j, H, W):
    result = [(i-1, j),
              (i, j - 1),  (i, j + 1),
              (i + 1, j)]
    return list(filter(lambda x: (0 <= x[0] <= (H-1)) and (0 <= x[1] <= (W-1)), result))


for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            eight = eight_math_index(i, j, H, W)
            shuui_kuro_kazu = 0
            for (k, l) in eight:
                if S[k][l] == "#":
                    shuui_kuro_kazu += 1
            if shuui_kuro_kazu == 0:
                print("No")
                exit(0)

print("Yes")
