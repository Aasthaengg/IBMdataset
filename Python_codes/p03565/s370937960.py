def restore(s, t):
    orig_s = s
    for i in range(len(s) - len(t), -1, -1):
        s = list(orig_s)
        ok = True
        for j in range(len(t)):
            if s[i+j] != t[j] and s[i+j] != '?':
                ok = False
                break
            s[i+j] = t[j]
        if ok:
            for i in range(len(s)):
                if s[i] == '?':
                    s[i] = 'a'
            return "".join(s)
    return "UNRESTORABLE"


S = input()
T = input()

print(restore(S, T))
