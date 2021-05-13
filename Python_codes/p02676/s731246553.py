k = int(raw_input())
s = raw_input()
l = len(s)
if k >= l:
    print(s)
else:
    ans = ""
    i = 0
    while i < k:
        ans += s[i]
        i += 1
    ans += "..."
    print(ans)
