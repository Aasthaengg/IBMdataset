s = input().strip()

ans = ""
for c in s :
    if c.islower() :
        ans += c.upper()
    else :
        ans += c.lower()
print(ans)
