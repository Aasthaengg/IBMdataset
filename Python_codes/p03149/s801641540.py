li = list(input())
lia = ['1','9','7','4']
from collections import Counter
c = Counter(li)
for i in lia:
    if c[i] != 1:
        print("NO")
        exit()
print("YES")