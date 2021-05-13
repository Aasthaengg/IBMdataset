from collections import Counter
a=input()
n=len(a)
d=Counter(a)

res = (n*(n-1))//2+1

for c in d.values():
    res -= (c*(c-1))//2
print(res)