s = list(input())
k = int(input())
t = sorted(s)
u = []
v = []
for i in range(min(len(s), 5)):
    u.append(t[i])
for i in range(len(s)):
    if s[i] in u:
        if not [s[i]] in v:
            v.append([s[i]])
        l = [s[i]]
        for j in range(1, 5):
            if i + j == len(s):
                break
            l = l + [s[i + j]]
            if not l in v:
                v.append(l)
for i in range(len(v)):
    v[i] = "".join(v[i])
v.sort()
print(v[k - 1])