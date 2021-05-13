s = list(input())
t = list(input())
for i in range((len(s))-(len(t)),-1,-1):
    for j in range(len(t)):
        if s[i+j] == "?":
            continue
        if s[i+j] != t[j]:
            break
    else:
        for k in range(len(t)):
            s[i+k] = t[k]
        for l in range(len(s)):
            if s[l] == "?":
                s[l] = "a"
        print("".join(s))
        break
else:
    print("UNRESTORABLE")