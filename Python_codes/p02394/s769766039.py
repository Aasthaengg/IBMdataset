# coding: utf-8
# Your code here!
# TP1_2_D

# 5 4 2 2 1
# 22 - 33
# 3 < 5　かつ　3<4だからOK

# 5 4 2 4 1
# 24 - 35
# 5がアウトる

# x,yがマイナスの場合も考慮したい


N = input().split()
# print(N)

W=int(N[0])
H=int(N[1])
x=int(N[2])
y=int(N[3])
r=int(N[4])

if x + r <= W and y + r <= H and x - r >= 0 and y - r >= 0:
    print("Yes")
else:
    print("No")
