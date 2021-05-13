s = input()
l = set(s)
ans = 10 ** 10
for x in l:
    cnt, cnt_max = 0, 0
    for i in s:
        if i != x:
            cnt += 1
        else:
            cnt_max = max(cnt_max, cnt)
            cnt = 0
    cnt_max = max(cnt_max, cnt)
    ans = min(cnt_max, ans)
print(ans)