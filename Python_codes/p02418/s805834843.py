s = input()
p = input()
for i in range(len(s)):
    if i + len(p) <= len(s):
        t = s[i:i + len(p)]
    else:
        t = s[i:] + s[:i + len(p) - len(s)]
    if t == p:
        print('Yes')
        break
else:
    print('No')