s = list(input())
compress = [s[0]]

ans = 0
for c in s:
    if c == compress[-1]:
        continue
    ans += 1
    compress.append(c)

print(ans)
