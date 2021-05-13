n = int(input())
s = input()
ec = 0
wc = 0
el = []
wl = []
for f,r in zip(s,reversed(s)):
    el.append(ec)
    wl.append(wc)
    if f == 'W':
        wc += 1
    if r == 'E':
        ec += 1

ans = n
for e,w in zip(wl, reversed(el)):
    ans = min(ans, e+w)

print(ans)