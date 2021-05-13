S = input()
T = input()
f = "UNRESTORABLE"

# 後ろから見ていって、部分文字列を当てはめる
S_r = S[::-1]
T_r = T[::-1]
for i in range(len(T),len(S)+1):
    S_ = S_r[i-len(T):i]
    flg = True
    for t,s in zip(T_r, S_):
        if s != "?" and s != t:
            flg = False
    if flg:
        ans = S_r[:i-len(T)] + T_r + S_r[i:]
        print(ans[::-1].replace("?","a"))
        exit()
print(f)
