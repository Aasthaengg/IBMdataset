# https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_c

from collections import Counter, defaultdict

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
c = defaultdict(int)
for row in A:
    for ch in row:
        c[ch] += 1

# 両方偶数 = 全部4回ずつ必要
if H % 2 == 0 and W % 2 == 0:
    if all(v % 4 == 0 for v in c.values()):
        print("Yes")
    else:
        print("No")
    exit()

# 両方奇数 (縦・横の中心がある)
elif H % 2 == 1 and W % 2 == 1:
    c_odd = sum(1 if v % 2 == 1 else 0 for v in c.values())
    if c_odd == 1 and sum(1 if v % 4 == 2 else 0 for v in c.values()) <= (W // 2) + (H // 2):
        print("Yes")
    else:
        print("No")
    exit()

# 片方が奇数
else:
    if all(v % 2 == 0 for v in c.values()) and \
        sum(1 if v % 4 == 2 else 0 for v in c.values()) <= \
            (W // 2 if W % 2 == 0 else H // 2):
        print("Yes")
    else:
        print("No")
    exit()