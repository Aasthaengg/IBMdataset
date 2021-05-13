x = input()

pair_cnt = 0
s_cnt = 0
for i in x:
    if i == "S":
        s_cnt += 1
    elif i == "T" and s_cnt:
        pair_cnt += 1
        s_cnt -= 1

print(len(x) - pair_cnt * 2)