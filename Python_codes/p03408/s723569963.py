import collections
n=int(input())
s = [input() for _ in range(n)]
m=int(input())
m = [input() for _ in range(m)]
dd = collections.defaultdict(int)
for i in s:
    dd[i]+=1
for i in m:
    dd[i]-=1
print(max(0,max(dd.values())))
