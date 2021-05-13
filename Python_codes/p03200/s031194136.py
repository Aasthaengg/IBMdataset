s = input()
count_w, ans= 0, 0
for i in range(len(s)):
    if s[i] == 'W':
        ans += i - count_w
        count_w += 1
print(ans)