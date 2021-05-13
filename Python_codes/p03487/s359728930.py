n = int(input())

al = list(map(int, input().split()))

import collections

c = collections.Counter(al)

res = 0
temp =0
for i in range(1,n+1):
    if c[i] ==0:
        pass
    elif c[i] ==i:
        temp += c[i]
        pass
    else:
        temp += c[i]
        if c[i] >i:
            res += c[i]-i
        else :
            res +=c[i]

res += (n-temp)
print(res)