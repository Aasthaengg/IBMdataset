from collections import Counter
N = int(input())
A = list(map(int,input().split()))

d = []
for key,value in Counter(A).items():
    if value >=4 :
        d.append(key)
        d.append(key)
    if value >= 2:
        d.append(key)

if len(d) < 2:
    print(0)
else:
    d = sorted(d,reverse=True)
    x = d[0]
    y = d[1]

    print(x*y)