n = int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))

d1 = {}
for d in D:
    if d not in d1:
        d1[d] = 1
    else:
        d1[d] += 1
d2 = {}
for t in T:
    if t not in d2:
        d2[t] = 1
    else:
        d2[t] += 1

for k2, v2 in d2.items():
    if k2 not in d1:
        print('NO')
        exit()
    else:
        v1 = d1[k2]
        if v1 < v2:
            print('NO')
            exit()
else:
    print('YES')
