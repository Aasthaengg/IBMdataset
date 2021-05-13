from collections import Counter
from bisect import bisect_right as br
n,a,b = map(int,input().split())
v = list(map(int,input().split()))
count = Counter(v)
v.sort()
c = 0

ans = sum(v[-a:])

def pascla(low):
    list=[[1],[1,1]]
    if low==0 or low==1:
        return list
    while low-len(list):   
        for i in list[-1:]:
            counter = len(i)-1
            locallist = []
            for j in range(counter):
                locallist.append(i[counter-1] + i[counter])
                counter-=1
            locallist.append(1)
            locallist.insert(0,1)
            list.append(locallist)           

    return list

comb = pascla(51)
for i in range(a,b+1):
    if sum(v[-i:])*a == ans*i:
        m = v[-i]
        if count[m] == 1:
            c += 1
        else:
            index = br(v,m)
            c += comb[count[m]][index-(n-i)]
print(ans/a)
print(int(c))
