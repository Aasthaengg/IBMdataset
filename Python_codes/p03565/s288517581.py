s = str(input())
t = str(input())
l = []
for i in range(len(s)-len(t)+1):
    num = 0
    for h in range(len(t)):
        if s[i+h] == t[h] or s[i+h] == '?':
            num += 1
        elif s[i+h] != t[h]:
            break
    if num == len(t):
        w2 = s[:i] + t + s[i + len(t):]
        w = ""
        for j in range(len(w2)):
            if w2[j] == "?":
                w += "a"
            else:
                w += w2[j]
        l.append(w)
l.sort()
if 0 < len(l):
    print(l[0])
else:
    print("UNRESTORABLE")