s = input()
i = 0
start = 0
pre = ""
ans = 0
while i < len(s):
    if i < len(s) and s[start: i + 1] != pre:
        pre = s[start: i + 1]
        start = i + 1
        ans += 1
    i += 1
print(ans)
