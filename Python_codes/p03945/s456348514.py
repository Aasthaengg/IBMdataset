s = input()

ans = 0
tmp = s[0]
for x in s[1:]:
    if x != tmp:
        ans += 1
        tmp = x

print(ans)