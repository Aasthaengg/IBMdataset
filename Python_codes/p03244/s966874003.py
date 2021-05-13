from collections import Counter
n = int(input())
v = list(map(int, input().split()))
l1 = []
l2 = []
for i in range(n):
    if i % 2 == 0:
        l1.append(v[i])
    else:
        l2.append(v[i])
if Counter(l1).most_common()[0][0] != Counter(l2).most_common()[0][0]:
    print(len(l1)-Counter(l1).most_common()[0][1]+len(l2)-Counter(l2).most_common()[0][1])
elif min(len(set(l1)), len(set(l2))) >= 2:
    print(min(len(l1)-Counter(l1).most_common()[0][1]+len(l2)-Counter(l2).most_common()[1][1], len(l1)-Counter(l1).most_common()[1][1]+len(l2)-Counter(l2).most_common()[0][1]))
elif len(set(l1)) > 1:
    print(len(l1)-Counter(l1).most_common()[1][1]+len(l2)-Counter(l2).most_common()[0][1])
elif len(set(l2)) > 1:
    print(len(l1)-Counter(l1).most_common()[0][1]+len(l2)-Counter(l2).most_common()[1][1])
else:
    print(n//2)