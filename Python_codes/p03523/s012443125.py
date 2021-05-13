s = input()
l = len(s)
f = 0
if l <= 9:
    for i in range(1 << l + 1):
        ans = ""
        for j in range(l + 1):
            if i >> j & 1: ans += 'A'
            if j < l: ans += s[j]
        if ans == "AKIHABARA":
            f = 1
else: f = 0

if f: print("YES")
else: print("NO")
