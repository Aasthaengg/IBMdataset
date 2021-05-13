from collections import Counter
N = int(input())
A = [int(i) for i in input().split()]
c = dict(Counter(A))
count = 0
for k in c.keys():
    if c[k] % 2 == 0:
        count += 1
print(len(c)-count % 2)
