s = input()
s = s.replace("dream", "D")
s = s.replace("erase", "E")
s = s.replace("Der", "D")
s = s.replace("Er", "E")

s = list(set(s))
ok = True
for i in range(len(s)):
    if s[i] not in ["D","E"]:
        ok = False
print("YES" if ok else "NO")