n, y = (int(x) for x in input().split())
a = 0
b = 0
c = 0
flag = 0


for s in range(n+1):
    if y-s*10000 == 0 and s == n and flag == 0:
        a = s
        print(a, b, c)
        flag = 1
    else:
        for t in range(n-s+1):
            if y-s*10000-t*5000-(n-s-t)*1000 == 0 and n-s-t >= 0 and flag == 0:
                a = s
                b = t
                c = n-s-t
                print(a, b, c)
                flag = 1
if flag == 0:
    print(-1, -1, -1)
