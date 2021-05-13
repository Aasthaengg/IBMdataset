
s = input()
i, ans, total = 0, 0, 0

while i < len(s) - 1:
    if s[i: i + 2] == "BC":
        ans += total 
        i += 2
    elif s[i] == "A":
        total += 1
        i += 1
    else:
        total = 0
        i += 1

print(ans)