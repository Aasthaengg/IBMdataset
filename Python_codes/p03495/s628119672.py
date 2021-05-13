from collections import Counter
n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
if n<=k:
    print(0)
else:    
    c = Counter(a)
    l = sorted(list(c.values()))
    print(sum(l[:-k]))