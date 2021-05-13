N = int(input())
A = list(map(int, input().split()))

import collections
dic=dict(collections.Counter(A))
li=list(dic.values())

ans='No'

if len(li)==3:
    if N%3 == 0:
        x,y,z = dic.keys()
        if li[0]== N//3 and li[1]==N//3 and x^y== z:
            ans='Yes'           
elif len(li)==2:
    if N%3 == 0:
        if li[0]== 2*N//3 or li[1]==2*N//3:
            ans='Yes'
elif len(li)==1:
        if list(dic.keys())[0]==0:
            ans='Yes'

print(ans)