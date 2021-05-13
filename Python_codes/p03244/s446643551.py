from collections import Counter
n = int(input())
v = list(map(int,input().split()))
a = []
b = []
for i in range(n):
    if i % 2 == 0:
        a.append(v[i])
    else:
        b.append(v[i])
c1 = Counter(a).most_common()
c2 = Counter(b).most_common()
if len(set(a)) == len(set(b)) == 1:
    if a == b:
        print(len(a))
    else:
        print(0)
else:
    if c1[0][0] != c2[0][0]:
        print(n - c1[0][1] - c2[0][1])
    else:
        print(min(n-c1[0][1] -c2[1][1],n - c1[1][1] - c2[0][1]))