"""
・全探索してもよい
・ある値（例えばa1）を決めたら他の値は全部決まってしまう
→ a1に適当な値を入れて後は全部できているかチェックすればよい
"""
import sys

c = [[int(i) for i in input().split()] for j in range(3)]
a = [0] * 3
b = [0] * 3

max_val = 100

# a1を適当に決める
a[0] = 0

# 他の値は勝手に決まる
b[0] = c[0][0] - a[0]
b[1] = c[0][1] - a[0]
b[2] = c[0][2] - a[0]
a[1] = c[1][0] - b[0]
a[2] = c[2][0] - b[0]

#print(f"a;{a}\t b:{b}")

for i in range(3):
    for j in range(3):
        left = a[i] + b[j]
        right = c[i][j]
        #print(f"{a[i]}+{b[j]} -> {c[i][j]}")
        if(left != right):
            ans = False
            print("No")
            sys.exit()


print("Yes")