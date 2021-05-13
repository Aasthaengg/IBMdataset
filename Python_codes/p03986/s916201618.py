s = input().rstrip()
n = len(s)

removed = 0
cnt_s = 0

for i in range(n):
    if s[i] == 'S':
        cnt_s += 1
    elif cnt_s:
        cnt_s -= 1
        removed += 1
#     print(cnt_s,cnt_t)
print(n - removed*2)