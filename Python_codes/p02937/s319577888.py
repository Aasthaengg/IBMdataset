from collections import defaultdict
from bisect import bisect_right
s,t=input(),input()
m=len(s)

dictionary=defaultdict(list)
for i,j in enumerate(s):
    dictionary[j] +=[i+1]

index,ans=0,0
for i in t:
    try:
        point=bisect_right(dictionary[i],index)
        if point==len(dictionary[i]):num=dictionary[i][0]
        else:num=dictionary[i][point]

        if index>=num:
            ans +=m
        index=num
    except:print(-1);exit()

print(ans+index)