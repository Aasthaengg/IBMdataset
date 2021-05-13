s = input()

if len(s) == 2:
    print(1)
else:
    while len(s) > 2:
        s = s[:-2]
        n = len(s) // 2
        if s[:n] == s[n:]:
            print(len(s))
            exit(0)
    print(1)
