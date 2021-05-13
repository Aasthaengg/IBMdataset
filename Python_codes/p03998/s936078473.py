s = {'a':input(), 'b':input(), 'c':input()}
t = 'a'
while s[t] != '':
    tmp = s[t][0]
    s[t] = s[t][1:]
    t = tmp
print(t.upper())