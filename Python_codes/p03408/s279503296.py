n = int(input())
b = [input() for i in range(n)]


m = int(input())
r = [input() for i in range(m)]

from collections import Counter
bc = Counter(b)
rc = Counter(r)

bs = list(set(b))

res = 0
for i in bs:
    res = max(res,bc[i]-rc[i])
    
print(res)