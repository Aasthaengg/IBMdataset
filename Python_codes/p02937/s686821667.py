import bisect

s = input()
t = input()
ls = len(s)
sets = set(s)
sett = set(t)
ind = [[] for _ in range(26)]
temp = 0
ans = 0
if sett.issubset(sets) == False:
    print('-1')
else:
    for i in range(ls):
        ind[ord(s[i])-97].append(i+1)
    for x in t:
        if temp >= ind[ord(x)-97][-1]:
            ans += ls - temp + ind[ord(x)-97][0]
            temp = ind[ord(x)-97][0]
        else:
            bs = bisect.bisect_right(ind[ord(x)-97],temp)
            ans += ind[ord(x)-97][bs] - temp
            temp = ind[ord(x)-97][bs]
    print(ans)