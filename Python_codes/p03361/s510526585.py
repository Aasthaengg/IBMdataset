import itertools
import sys

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for i, j in itertools.product(range(H), range(W)):  # jが先に増える
    c = 0
    if S[i][j] == "#":
        if i != 0 and S[i - 1][j] == "#":
            c += 1

        if i != H - 1 and S[i + 1][j] == "#":
            c += 1

        if j != 0 and S[i][j - 1] == "#":
            c += 1

        if j != W - 1 and S[i][j + 1] == "#":
            c += 1

        if c == 0:
            print("No")
            sys.exit()
            break
else:
    print("Yes")
