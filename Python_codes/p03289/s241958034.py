s = list(input())
ans = "WA"

if s[0] == "A":
    if s[2:-1].count("C") == 1:
        s.remove("C")
        k = "".join(s[1:])
        if k.islower():
            ans = "AC"
print(ans)