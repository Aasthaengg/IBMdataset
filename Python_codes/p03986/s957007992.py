s = input()
s_cnt = puyo = 0
for si in s:
    if si == "S": s_cnt += 1
    elif s_cnt > 0:
        s_cnt -= 1
        puyo += 1
print(len(s) - puyo * 2)