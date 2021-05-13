s = input()[::-1]
t = input()[::-1]
if len(s) < len(t):
    print("UNRESTORABLE")
    exit()
    
tmp = s.replace("?", "a")
if t in tmp:
    print(tmp[::-1])
    exit()
    
for i in range(len(s) - len(t) + 1):
    for j in range(len(t)):
        if s[i + j] == "?":
            continue
        elif s[i + j] == t[j]:
            continue
        break
    else:
        ans = ""
        for k in range(i):
            if s[k] == "?":
                ans += "a"
            else:
                ans += s[k]
        for tt in t:
            ans += tt
        for k in range(len(t) + i, len(s)):
            if s[k] == "?":
                ans += "a"
            else:
                ans += s[k]
        print(ans[::-1])
        exit()
print("UNRESTORABLE")