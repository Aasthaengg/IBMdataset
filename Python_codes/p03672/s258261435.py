s = input()
while 1:
    s = s[:-1]
    if len(s) % 2 == 1:
        continue
    else:
        h = len(s) // 2
        if s[:h] == s[h:]:
            break
print(len(s))
