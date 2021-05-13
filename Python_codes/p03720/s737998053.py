n,m,*ab = map(int, open(0).read().split())

from collections import Counter

c = Counter(ab)

for i in range(1,n+1):
    print(c[i])