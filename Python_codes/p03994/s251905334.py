# 必要な回数を連想配列で対応付ける。
alpha = "bcdefghijklmnopqrstuvwxyza"
last_process = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
need_char_point = {}
need_point_char = {}
pointa = 0
for i in reversed(range(len(alpha))):
    need_char_point[alpha[pointa]] = i
    need_point_char[i] = alpha[pointa]
    pointa += 1

# print(need_point)
s = str(input())
k = int(input())
ans = ""
for i in range(len(s)):
    if k >= need_char_point[s[i]]:
        k -= need_char_point[s[i]]
        ans += "a"
    else:
        ans += s[i]
if k > 0:
    k %= 26
    for i in range(len(last_process)):
        if ans[-1] == last_process[i]:
            tmp = i
            break
    hoge = list(ans)
    hoge[-1] = last_process[tmp+k]
    ans = "".join(hoge)

print(ans)
