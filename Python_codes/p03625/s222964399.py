from collections import Counter
n = int(input())
a = list(map(int,input().split()))
c = Counter(a)
d = [0,0]
for i in c:
    if c[i]>1:
        d.append(i)
    if c[i]>3:
        d.append(i)
d.sort()
print(d[-1]*d[-2])