# 2020/07/26
# AtCoder Beginner Contest 066 - B
# B:後ろから順に消して全探索
# 2文字ずつ消す

# Input
s = list(input())
n = len(s)

# Calc
for i in range(n-1, 0, -1):
    s.pop()
    slen = len(s)
    # 偶数時のみ実施
    if slen % 2 == 0:
        hs = slen // 2
        tflg = True
        for j in range(0, hs, 1):
            if s[j] != s[j+hs]:
                tflg = False
                break
        if tflg == True:
            ans = slen
            break

# Output
print(ans)
