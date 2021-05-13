s = input().replace('BC', 'X')
cnt_a = 0
ans = 0
for c in s:
    if c == 'A':
        cnt_a += 1
    if c == 'X':
        ans += cnt_a
    if c in 'BC':
        cnt_a = 0
print(ans)
