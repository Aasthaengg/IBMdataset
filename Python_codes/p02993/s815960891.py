s = input()
ans = "Good"

if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
    ans = "Bad"

print(ans)
