s = input()
t = input()
maxs = 0
if len(s) == len(t):
    c = 0
    for k in range(len(t)):
        if s[k] == t[k]: c += 1
    print(len(t) - c)
    quit()
for i in range(len(s)-len(t)):
    c = 0
    for k in range(len(t)):
        if s[i+k] == t[k]: c += 1
    maxs = max(c,maxs)
print(len(t) - maxs)