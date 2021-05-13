s = input().rstrip()
n = len(s)

removed = 0
cnt_s = cnt_t = 0

for i in range(n):
    if s[i] == 'S':
        cnt_s += 1
    else:
        cnt_t += 1
    if i == n-1:
        removed += min(cnt_s,cnt_t)
    elif cnt_t > cnt_s:
        removed += cnt_s
        cnt_s = cnt_t = 0
#     print(cnt_s,cnt_t)
print(len(s) - removed*2)