from collections import Counter
n = int(input())
v = list(map(int,input().split()))

if len(set(v)) == 1:
    print(n//2)
else:

    c1 = Counter(v[::2])
    c2 = Counter(v[1::2])
    o = c1.most_common(2)
    e = c2.most_common(2)
    o.append((0,0))
    e.append((0,0))
    if o[0][0] == e[0][0]:
        print(min(n-o[1][1]-e[0][1],n-o[0][1]-e[1][1]))
    else:
        print(n-o[0][1]-e[0][1])