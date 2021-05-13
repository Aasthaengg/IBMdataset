s, t = input(), input()
for i in range(len(t)):
    if s == t:
        print('Yes')
        exit()
    s = s[1:] + s[:1]
print('No')