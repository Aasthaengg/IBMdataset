s = input()

ans = 0
bef = s[0]
for c in s[1:]:
    if bef != c:
        ans += 1
    bef = c

print(ans)
