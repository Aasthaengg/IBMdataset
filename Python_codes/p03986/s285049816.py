s = input().rstrip()

removed = 0
cnt_s = cnt_t = 0

for c in s:
    if c == 'S':
        cnt_s += 1
    else:
        cnt_t += 1
    if cnt_t > cnt_s:
        removed += cnt_s
        cnt_s = cnt_t = 0
#     print(cnt_s,cnt_t)
removed += min(cnt_s,cnt_t)
print(len(s) - removed*2)