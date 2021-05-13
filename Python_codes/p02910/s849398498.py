s = input()
ans = "Yes"
if "L" in s[::2]:
    ans = "No"
if "R" in s[1::2]:
    ans = "No"
print(ans)