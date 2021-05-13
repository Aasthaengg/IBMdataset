N = int(input())
P = list(map(int, input().split()))
p0 = 0
p1 = P[0]
temp = []
for i, p in enumerate(P[1:]):
    if p >= p1:
        p0 = p1
        p1 = p
        continue
    else:
        temp.append(i)
        p1 = p

if len(temp) == 2:
    P[temp[0]], P[temp[1]+1] = P[temp[1]+1], P[temp[0]]

    p0 = 0
    p1 = P[0]
    temp = []
    for i, p in enumerate(P[1:]):
        if p >= p1:
            p0 = p1
            p1 = p
            continue
        else:
            temp.append(i)
            p1 = p
    if len(temp) == 0:
        print("YES")
    else:
        print("NO")
elif len(temp)==0:
    print("YES")
else:
    print("NO")
