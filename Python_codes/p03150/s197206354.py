s = input()
ans = "NO"
if s[:7]== "keyence" or s[:-7] == "keyence":
    ans = "YES"
else:
    a = "keyence"
    for i in range(7):
        if s[:i]+s[-7+i:] == a: ans = "YES"
print(ans)