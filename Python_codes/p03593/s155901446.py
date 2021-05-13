# -*- coding: utf-8 -*-
import collections
h, w = map(int,input().split())
a = []
for i in range(h):
    a.append(list(input()))

tmp = []
for i in range(h):
    for j in a[i]:
        tmp.append(j)
#print(tmp)
c = collections.Counter(tmp)
tmp2 = list(set(tmp))
four = 0
two = 0
odd = 0
for i in tmp2:
    if c[i] % 4 == 0:
        four += 1
    elif c[i] % 2 == 0:
        two += 1
    else:
        odd += 1

if h % 2 == 1 and w % 2 == 1:
    if odd == 1 and two <= (h // 2 + w // 2):
        ans = "Yes"
    else:
        ans = "No"
elif h % 2 == 0 and w % 2 == 0:
    if two == 0 and odd == 0:
        ans = "Yes"
    else:
        ans = "No"
elif h % 2 == 0 and w % 2 == 1:
    if odd == 0 and two <= h // 2:
        ans = "Yes"
    else:
        ans = "No"
elif h % 2 == 1 and w % 2 == 0:
    if odd == 0 and two <= w // 2:
        ans = "Yes"
    else:
        ans = "No"
print(ans)
