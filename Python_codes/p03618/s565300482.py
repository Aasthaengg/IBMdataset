from collections import Counter
a = input()
n = len(a)
c = Counter(a)
# print(c.keys())
tp = 0
for val in c.values():
    tp += (val*(val-1))//2

print((n*(n-1)//2)-tp+1)


