s = input()

while len(s) > 2:
    s = s[:-2]
    n = len(s) // 2
    if s[:n] == s[n:]:
        print(len(s))
        exit(0)
print(1)
