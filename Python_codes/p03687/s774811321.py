import collections
s = input()
ls = len(s)
c = collections.Counter(s)
mi = ls
valuePlaces = []
for v,k in c.items():
    co = 0
    valuePlaces.clear()
    for i in range(ls):
        if s[i] == v:
            valuePlaces.append(i)
    ushiro = ls-valuePlaces[-1]-1
    #print(ushiro,v)
    maxLen = 0
    len_vp = len(valuePlaces)
    #print(len_vp)
    for i in range(len_vp):
        start = valuePlaces[i]
        if i == 0:
            goal = -1
        else:
            goal = valuePlaces[i-1]
        maxLen = max(start-goal-1,maxLen)
    mi = min (mi,max(maxLen,ushiro))
print(mi)



