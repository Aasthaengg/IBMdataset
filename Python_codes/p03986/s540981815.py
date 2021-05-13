X = input()
"""
Tの前にSがどれだけあるか？
TSSTTTSS
"""
s_cnt = 0
t_cnt = 0
cnt = 0
for s in X:
    if s == "S":
        s_cnt += 1
    if s == "T":
        t_cnt += 1
        if t_cnt <= s_cnt:
            cnt += 2
        else:
            s_cnt = 0
            t_cnt = 0


print(len(X) - cnt)
