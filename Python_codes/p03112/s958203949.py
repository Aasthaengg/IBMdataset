a,b,q=map(int,input().split())

s=[int(input()) for _ in range(a)]
t=[int(input()) for _ in range(b)]
x=[int(input()) for _ in range(q)]

s.sort()
t.sort()

import bisect
#a=[0,2,3,4,67,8]
#a.sort()
for item in x:
    ss=bisect.bisect_left(s, item)
    tmp=[]
    if ss>0:
        tmp.append(s[ss-1])
    if ss<len(s):
        tmp.append(s[ss])
    tmp2=[]
    tt=bisect.bisect_left(t, item)
    if tt>0:
        tmp2.append(t[tt-1])
    if tt<len(t):
        tmp2.append(t[tt])
    #print(item,tmp2,tmp)
    result=10**18
    for item2 in tmp:
        for item3 in tmp2:
            #print(item,item2,item3)
            result=min(result,abs(item-item3)+abs(item3-item2),abs(item-item2)+abs(item3-item2))
    print(result)



