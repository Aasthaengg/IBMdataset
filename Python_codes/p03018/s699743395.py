s = input()
s = s.replace("BC","D")
ans = 0
a = 0
for k in range(len(s)):
    if s[k] == "A":
        a += 1
    elif s[k] == "D":
        ans += a
    else:
        a = 0
print(ans)
