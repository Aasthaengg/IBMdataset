import bisect
s = input()
t = input()
d = {}
if set(t) <= set(s):
    for c in set(s):
        d[c] = []
    for i,c in enumerate(s):
        d[c].append(i)
    ret = 0
    for i,c in enumerate(t):
        if i==0:
            loc = d[t[0]][0]
        else:
            nx_idx = bisect.bisect_right(d[c], loc)
            if nx_idx == len(d[c]):
                ret += 1
                nx_idx = 0
            nx_loc = d[c][nx_idx]
            loc = nx_loc
    print(ret*len(s) + loc + 1)
else:
    print(-1)
