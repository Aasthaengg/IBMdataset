s = input()
ans = 0
for i in range(len(s)):
    if i % 2 == 0 and s[i] == "p":
        ans -= 1
    elif i % 2 == 1 and s[i] == "g":
        ans += 1
print(ans)
