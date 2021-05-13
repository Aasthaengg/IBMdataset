s = input()
t = input()
ls = len(s)
s += s[0:len(t)]
f = 0
i = 0
while i < ls:
    if t == s[i:i+len(t)]:
        f = 1
        break
    i += 1
if f == 0:
    print('No')
else:
    print('Yes')
