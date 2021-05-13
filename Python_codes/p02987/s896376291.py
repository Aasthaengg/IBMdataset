s = list(input())
ans = "Yes"
s.sort()
if s[0] != s[1]:
    ans = "No"
elif s[2] != s[3]:
    ans = "No"
if s[0] == s[2]:
    ans = "No"
print(ans)