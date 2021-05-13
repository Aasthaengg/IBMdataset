from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
count = 0
for v in c.values():
    if v != 1:
        count += v-1
#print(count)
if count % 2 == 0:
    print(len(c.keys()))
else:
    print(len(c.keys())-1)

