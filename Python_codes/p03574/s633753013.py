import numpy as np

H, W = list(map(int, input().split()))
S = ["." + input() + "." for i in range(H)]
S = ["." * (W + 2)] + S + ["." * (W + 2)]
# print(H)
# print(W)
a = []
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if S[i][j] == ".":
            # print(i, j, S[i][j])
            tmp = S[i - 1][j - 1] + S[i - 1][j] + S[i - 1][j + 1] + S[i][j -
                                                                         1] + S[i][j + 1] + S[i + 1][j - 1] + S[i + 1][j] + S[i + 1][j + 1]
            c = str(tmp.count("#"))
            a.append(c)
        else:
            a.append("#")

a = np.reshape(a, (H, W))
for raw in a:
    ls = ""
    for item in raw:
        ls += item
    print(ls)
