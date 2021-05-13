seq = input()

ans = ""

for s in seq:
    if s == "?":
        ans += "D"
    else:
        ans += s

print(ans)