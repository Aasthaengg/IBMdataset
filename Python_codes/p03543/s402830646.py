s = input()

ans = "No"
if s[1] == s[2] and (s[0] == s[1] or s[2] == s[3]):
    ans = "Yes"

print(ans)
