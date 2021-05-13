from collections import defaultdict
n = int(input())
v = list(map(int, input().split()))
even = [[0,i] for i in range(10**5+5)]
odd = [[0,i] for i in range(10**5+5)]
numnum = 0
for i in range(n):
    if even[v[i]][0] == 0 and odd[v[i]][0] == 0:
        numnum += 1
    if i % 2 == 0:
        even[v[i]][0] += 1
    else:
        odd[v[i]][0] += 1
if numnum == 1:
    print(n // 2)
    exit()
even.sort(key=lambda x:x[0], reverse=True)
odd.sort(key=lambda x:x[0], reverse=True)
if n == 2:
    print(0)
    exit()
e0, e1, o0, o1 = even[0][1], even[1][1], odd[0][1], odd[1][1]
if e0 != o0:
    print(n - even[0][0] - odd[0][0])
elif e0 != o1 and e1 != o0:
    print(min(n - even[0][0] - odd[1][0], n - even[1][0] - odd[0][0]))
elif e0 != o1:
    print(n - even[0][0] - odd[1][0])
else:
    print(n - even[1][0] - odd[0][0])