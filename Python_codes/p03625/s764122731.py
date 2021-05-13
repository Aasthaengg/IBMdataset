from collections import Counter
n = int(input())
a = list(map(int,input().split()))
c = Counter(a)
s = sorted(list(set(a)),reverse=True)
x = []
ans = 0
for si in s:
    if len(x)>=2:
        break
    cs=c[si]
    if cs>=4:
        x.append(si)
        x.append(si)
    elif cs>=2:
        x.append(si)
if len(x)<=1:
    print(0)
else:
    print(x[0]*x[1])