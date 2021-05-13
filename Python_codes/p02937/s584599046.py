from bisect import bisect_left
s = input()
t = input()
dic = {}
for ind, c in enumerate(s):
    if c in dic:
        dic[c].append(ind)
    else:
        dic[c] = [ind]
loop = 0
ind = 0
try:
    for c in t:
        if ind > dic[c][-1]:
            ind = dic[c][0] + 1
            loop += 1
            continue
        tmp = bisect_left(dic[c], ind)
        ind = dic[c][tmp] + 1
    print(len(s)*loop+ind)
except:
    print(-1)