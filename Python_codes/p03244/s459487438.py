n = int(input())
v  = list(map(int, input().split()))
a = [v[i] for i in range(0, n, 2)]
b = [v[i] for i in range(1, n, 2)]
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
e = {}
for i in b:
    if i not in e:
        e[i] = 1
    else:
        e[i] +=1
d = sorted(d.items(), key=lambda x: -x[1])
e = sorted(e.items(), key=lambda x: -x[1])
if d[0] != e[0]:
    print(n-d[0][1]-e[0][1])
else:
    if len(d) == len(e) == 1:
        print(n//2)
    elif len(d) == 1 and len(e) > 1:
        print(n//2-e[1][1])
    elif len(d) > 1 and len(e) == 1:
        print(n//2-d[1][1])
    else:
        print(n-max(d[0][1]+e[1][1], d[1][1]+e[0][1]))
