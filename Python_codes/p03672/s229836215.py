s = list(str(input()))
for i in range(len(s)):
    s.pop()
    if len(s)%2 == 1:
        continue
    t = s[0:len(s)//2]
    u = s[len(s)//2:]
    t = ''.join(t)
    u = ''.join(u)
    if t == u:
        print(len(s))
        exit()
