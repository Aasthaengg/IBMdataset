import math
s = int(input())

"""
p1を原点、p2を10**9、1に固定する
S = 10**9*y3 - x3
v = 10**9 として
を満たすy3, x3を探せばよい
s%v = 0 - x3
s%v = v-x3
x3 = (v-s%v)%v # 外側の%vは括弧が負の場合の対策

s//v = y3 - x3//v
(s+x3)//v = y3
"""
v = 10**9
ans = [0] * 6
ans[0], ans[1] = 0, 0
ans[2], ans[3] = 10**9, 1
ans[4] = (v-s%v)%v
ans[5] = (s+ans[4])//v

print(' '.join(list(map(str, ans))))
