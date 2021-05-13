s = input()
alp = 'abcdefghijklmnopqrstuvwxyz'
if len(s) < 26:
    for a in alp:
        if a not in s:
            print(s + a)
            exit()
else:
    for i in range(25, 0, -1):
        if s[i - 1] < s[i]:
            c = 'ω'
            for j in range(i, 26):
                if s[i - 1] < s[j]:
                    c = min(c, s[j])
            print(s[:i-1] + c)
            exit()

    print(-1)
