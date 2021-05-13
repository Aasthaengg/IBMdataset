n = int(input())
XY = []
for i in range(n):
    x, y = map(int, input().split())
    XY.append((x, y))

if n == 1:
    print(1)
    exit()
    
D = {}
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        a = XY[i][0]
        b = XY[i][1]
        c = XY[j][0]
        d = XY[j][1]
        p = c-a
        q = d-b
        if (p, q) in D:
            D[(p, q)] += 1
        else:
            D[(p,q)] = 1

D = list(D.items())
D.sort(key = lambda x: -x[1])
print(n-D[0][1])
