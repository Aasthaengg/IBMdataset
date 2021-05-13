import sys
import re
s = input()
x, y = [int(i) for i in sys.stdin.readline().split()]
s = [len(i) for i in re.split("T", s)]
v_ls = s[1::2]
h_ls = s[::2]
x -= h_ls[0]
h_ls.pop(0)
v_sum = sum(v_ls)
h_sum = sum(h_ls)
# memo_v_ls[i][j] : i番目まででj - v_sumができるか
width = max(abs(y), v_sum)
memo_v_ls = [[0 for i in range(width * 2 + 1)] for j in range(len(v_ls) + 1)]
memo_v_ls[0][width] = 1
for j, v in enumerate(v_ls, 1):
    for i in range(width * 2 + 1):
        if i >= v and i <= 2 * width - v:
            memo_v_ls[j][i] = max(memo_v_ls[j - 1][i - v], memo_v_ls[j - 1][i + v])
        elif i >= v:
            memo_v_ls[j][i] = memo_v_ls[j - 1][i - v]
        else:
            memo_v_ls[j][i] = memo_v_ls[j - 1][i + v]

flg = memo_v_ls[-1][y + width] == 1

width = max(abs(x), h_sum)
memo_h_ls = [[0 for i in range(width * 2 + 1)] for j in range(len(h_ls) + 1)]
memo_h_ls[0][width] = 1
for j, h in enumerate(h_ls, 1):
    for i in range(width * 2 + 1):
        if i >= h and i <= 2 * width - h:
            memo_h_ls[j][i] = max(memo_h_ls[j - 1][i - h], memo_h_ls[j - 1][i + h])
        elif i >= h:
            memo_h_ls[j][i] = memo_h_ls[j - 1][i - h]
        else:
            memo_h_ls[j][i] = memo_h_ls[j - 1][i + h]

flg &= memo_h_ls[-1][x + width] == 1
if flg:
    print("Yes")
else:
    print("No")