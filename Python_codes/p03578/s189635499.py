n=int(input())
*d,=map(int, input().split( ))
m=int(input())
*t,=map(int, input().split( ))
from collections import Counter

dc=Counter(d);tc=Counter(t)
for ti in tc:
    if ti not in dc:
        print("NO")
        exit()
    if dc[ti]<tc[ti]:
        print("NO")
        exit()
print('YES')