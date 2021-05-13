s = list(input())
t = list(input())

for i in range(len(t) - 1, len(s))[-1::-1]:
    if s[i] == "?" or t[-1]:
        jud = True
        for j in range(len(t)):
            if s[i - j] == t[-1 - j] or s[i - j] == "?":
                continue
            jud = False
            break
        if jud:
            for j in range(len(t)):
                s[i - j] = t[-1 - j]
            for j in range(len(s)):
                if s[j] == "?":
                    s[j] = "a"
            print("".join(s))
            exit()

print("UNRESTORABLE")