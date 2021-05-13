import sys
from collections import Counter
 
H, W = map(int, sys.stdin.readline().split())
 
string = ""
for _ in range(H):
    string += sys.stdin.readline().strip()
 
counter = Counter(string)
e_one = 0
e_two = 0
e_four = 0
for key, count in counter.items():
    tmp = count // 4
    e_four += tmp
    count -= 4 * tmp
    tmp = count // 2
    e_two += tmp
    count -= 2 * tmp
    e_one += count
 
one = 0
two = 0
four = 0
if H % 2 == 0 and W % 2 == 0:
    four = H * W // 4
# 奇数の場合、中心の文字は1つしかなくても回文になる
elif H % 2 == 1 and W % 2 == 1:
    one = 1
    two = H // 2 + W // 2
    four = (H * W - (one + two * 2)) // 4
else:
    # 縦を奇数とする
    if W % 2 == 1:
        H, W = W, H
 
    two = W // 2
    four = (H * W - two * 2) // 4
 
if four > e_four:
    print("No")
else:
    e_four -= four
    e_two += e_four * 2
    if two > e_two:
        print("No")
    else:
        e_two -= two
        e_one += e_two * 2
        if e_one == one:
            print("Yes")
        else:
            print("No")