from itertools import combinations
from collections import Counter
n = int(input())
C = Counter()
for i in range(n):
    C[input()[0]] +=1


print(sum(C[a]*C[b]*C[c] for a,b,c in combinations('MARCH',3)
))