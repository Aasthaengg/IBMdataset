s = input()
n = len(s)

ans = ""
i = 0
for _ in range(n):
    if i > n or ans == s: break
    if s[i:i+5] == "erase":
        i += 5
        ans += "erase"
        if s[i:i+1] == "r":
            i += 1
            ans += "r"
    elif s[i:i+5] == "dream":
        i += 5
        ans += "dream"
        if s[i:i+3] == "era": continue
        elif s[i:i+2] == "er":
            i += 2
            ans += "er"
print("YES" if ans == s else "NO")