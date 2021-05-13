s = list(input())
t = list(input())

n = len(s)
d = {}
d2 = {}

for i in range(n):
    if s[i] not in d:
        d[s[i]] = t[i]
    elif d[s[i]] != t[i]:
        print("No")
        exit()
    if t[i] not in d2:
        d2[t[i]] = s[i]
    elif d2[t[i]] != s[i]:
        print("No")
        exit()

print("Yes")
