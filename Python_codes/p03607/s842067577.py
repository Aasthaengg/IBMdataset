from collections import defaultdict
n = int(input())
a = defaultdict(int)
for _ in range(n):
    A = int(input())
    a[A] += 1
#print(a)
count = 0
for v in a.values():
    if v % 2 != 0:
        count += 1
print(count)