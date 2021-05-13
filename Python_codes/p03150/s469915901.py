s = list(input())
ls = len(s)
key = "keyence"
if "".join(s) == key:
    print("YES")
    exit()
f = False
for l in range(ls):
    for r in range(l + 1, ls):
        f |= "".join(["".join(s[:l]), "".join(s[r:])]) == key

print("YES" if f else "NO")
