s = input()
t = input()

l = len(s)
d1 = dict()
d2 = dict()

for i in range(l):
    if s[i] not in d1:
        d1[s[i]] = t[i]
    elif d1[s[i]] != t[i]:
        print("No")
        exit()

for i in range(l):
    if t[i] not in d2:
        d2[t[i]] = s[i]
    elif d2[t[i]] != s[i]:
        print("No")
        exit()

print("Yes")
