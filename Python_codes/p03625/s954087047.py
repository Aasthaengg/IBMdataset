from collections import Counter

n = int(input())
a = list(map(int, input().split()))

dic = Counter(a)

l = []
for i, j in dic.items():
    if j >= 4:
        l.append(i)
        l.append(i)
    elif j >= 2:
        l.append(i)

if len(l) < 2:
    print(0)
else:
    l.sort()
    print(l[-1] * l[-2])