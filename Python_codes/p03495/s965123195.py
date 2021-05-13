n,k = map(int, input().split())

al = list(map(int, input().split())) 


import collections

c = collections.Counter(al)

l = len(c)
cc = sorted(c.items(), key=lambda x:x[1])

res = 0

if l <= k:
    pass

else:
    for i in range(l-k):
       res += cc[i][1] 

print(res)