s = input()
ans = s
if len(s) == 3:
    ans = ''
    for i in range(3):
        ans += s[2-i]
print(ans)