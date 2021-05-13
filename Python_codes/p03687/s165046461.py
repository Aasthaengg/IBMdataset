import collections
s = input()
ls = len(s)
c = set(s)
mi = ls
valuePlaces = []
for v in c:
    co = 0
    valuePlaces.clear()
    for i in range(ls):
        if s[i] == v:
            valuePlaces.append(i)
    ushiro = ls-valuePlaces[-1]-1
    maxLen = 0
    len_vp = len(valuePlaces)
    for i in range(len_vp):
        start = valuePlaces[i]
        if i == 0:
            goal = -1
        else:
            goal = valuePlaces[i-1]
        maxLen = max(start-goal-1,maxLen)
    mi = min (mi,max(maxLen,ushiro))
print(mi)