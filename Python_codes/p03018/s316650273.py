s = input()
ind = 0
len_s = len(s)
string = ""
cnt = 0
ans = 0
while ind < len_s:
    _s = s[ind]
    if _s == "A":
        cnt += 1
        ind += 1
    elif _s == "B" and ind + 1 < len_s and s[ind + 1] == "C":
        ind += 2
        ans += cnt
    else:
        cnt = 0
        ind += 1

print(ans)