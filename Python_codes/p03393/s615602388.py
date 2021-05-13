s = input()
alp = list("abcdefghijklmnopqrstuvwxyz")
if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
elif len(s) < 26:
    for i in alp:
        if i not in s:
            print(s+i)
            break
else:
    ans = ""
    for i in range(len(s)-1):
        f = True
        for j in range(i, len(s)-1):
            if ord(s[j]) < ord(s[j+1]):
                f = False
                break
        if f:
            t = sorted(list(s[i:]))
            for k in t:
                if ord(s[i-1]) < ord(k):
                    print(s[:i-1] + k)
                    break
            exit()
    print(s[:-2] + s[len(s)-1])