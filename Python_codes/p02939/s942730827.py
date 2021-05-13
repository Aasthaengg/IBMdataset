s = input()
ans = 1
l = s[0]
cnt = 0
l_cnt = 0
for char in s[1:]:
    if (char == l and cnt == 0 and l_cnt== 0):
        cnt += 1
        continue
    else:
        l_cnt = cnt
        cnt = 0
        l = char
        ans += 1
print(ans)
