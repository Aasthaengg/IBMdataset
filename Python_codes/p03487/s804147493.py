import collections
n=int(input())
a=list(map(int,input().split()))
d=collections.Counter(a)
ans=0
for key,value in d.items():
    if key > value:
        ans += value
    if value > key:
        ans += (value - key)
print(ans)