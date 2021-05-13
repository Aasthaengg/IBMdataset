s = input()
f = s[0]
ans = "AC"

if "C" in s[2:-1] and f == "A" and s[2:-1].count("C") == 1:
    pass
else:
    ans = "WA"

for i in s:
    if i.isupper():
        if i == "A" or i == "C":
            continue
        else:
            ans = "WA"

print(ans)