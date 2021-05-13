from bisect import bisect_right
s = input()
t = input()

sdict = {}
for i,c in enumerate(s):
    if c not in sdict:
        sdict[c] = []
    sdict[c].append(i)

ans = 0
spos = -1
for c in t:
    if c not in sdict:
        print(-1)
        exit()
    tt = bisect_right(sdict[c], spos)
    if tt == len(sdict[c]):
        # print('-',tt)
        tt = bisect_right(sdict[c], -1)
        ans += len(s)
    # print(c, spos, sdict[c], tt)
    spos = sdict[c][tt]

print(ans + spos + 1)
