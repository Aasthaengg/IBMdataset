import bisect
s=input()
t=input()
alp=[[] for _ in range(26)]
flag=1
for i in range(len(s)):
    alp[ord(s[i])-97].append(i)
#print(alp)

idx=0
sets=0
i=0
while i<len(t):
    al=ord(t[i])-97
    if len(alp[al])==0:
        flag=0
        break
    else:
        if idx>alp[al][len(alp[al])-1]:
            sets=sets+1
            idx=-1
        else:
            idx=bisect.bisect_left(alp[al],idx)
            idx=alp[al][idx]+1
            i=i+1
    #print(sets,idx)
    #input()
if flag==1:
    print(sets*len(s)+idx)
else:
    print("-1")
"""
l=[0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    idx=bisect.bisect_left(l,i)
    idx2=bisect.bisect_right(l,i)
    print(l[idx],l[idx2])
"""