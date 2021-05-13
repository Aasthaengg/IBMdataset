s = list(input())
a = ["g"] * (-(-len(s) // 2)) + ["p"] * (len(s) // 2)
ans = 0
for i in range(len(s)):
    if s[i] == "g" and a[i] == "p":
        ans += 1
    elif s[i] == "p" and a[i] == "g":
        ans -= 1
print(ans)