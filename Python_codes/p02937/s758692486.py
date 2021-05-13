al = "abcdefghijklmnopqrstuvwxyz"
d = {}
dn = {}
for a in al:
    d[a] = []
    dn[a] = 0
s = input()
for i in range(len(s)):
    d[s[i]].append(i)
    dn[s[i]] += 1

t = input()
import bisect
ans = 0
n = -1
for a in t:
    l = d[a]
    if l:
        res = bisect.bisect(l, n)
        if res == dn[a]:
            ans += 1
            n = l[0]
        else:
            n = l[res]
    else:
        ans = 0
        n = -2
        break
print(ans * len(s) + n + 1)