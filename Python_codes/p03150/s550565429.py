s = input()
cond = False
key = "keyence"

for i in range(len(s)+1):
    for j in range(i, len(s)+1):
        mod_s = s[:i]+s[j:]
        if mod_s == key:
            cond = True


print("YES" if cond else "NO")
