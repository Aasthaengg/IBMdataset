s = input()
ans = 0
pre = ""
now = ""
for ss in s:
    now += ss
    if pre != now:
        ans += 1
        pre = now
        now = ""
print(ans)