road = []

road += input().split()
road += input().split()
road += input().split()

from collections import Counter

c = Counter(road)

flag = True
for k, v in c.items():
    if v > 2:
        flag = False

if flag:
    print("YES")
else:
    print("NO")
