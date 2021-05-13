s = input(); p = input()
for i in range(len(s)):
    sm = s[i:] + s[:i]
    if p in sm:
        print('Yes')
        exit()
print('No')
