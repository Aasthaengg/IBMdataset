s = input()
ans = 0
if int(s[0]) >= int(s[1]) and int(s[0]) >= int(s[2]):
    ans = int(s[0]) * 100 + int(s[0]) * 10 + int(s[0]) * 1
else:
    ans = int(s[0]) * 100 + int(s[0]) * 10 + int(s[0]) * 1 + 111
print(ans)