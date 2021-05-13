from collections import Counter
n = int(input())
a = [int(i) for i in input().split(" ")]
r = [i+1-j for i, j in enumerate(a)]
l = [j+i+1 for i, j in enumerate(a)]
nl = Counter(l)
nr = Counter(r)
 
ans = 0
for k, v in nl.items():
    ans += nr[k]*v
print(ans)