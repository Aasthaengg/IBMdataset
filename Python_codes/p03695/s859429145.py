n = int(input())
a = list(map(int,input().split()))

t = set()
c = 0
for i in range(n):
    if a[i] <= 399:
        t.add(1)
    elif a[i] <= 799:
        t.add(2)
    elif a[i] <= 1199:
        t.add(3)
    elif a[i] <= 1599:
        t.add(4)
    elif a[i] <= 1999:
        t.add(5)
    elif a[i] <= 2399:
        t.add(6)
    elif a[i] <= 2799:
        t.add(7)
    elif a[i] <= 3199:
        t.add(8)
    else:
        c += 1
s = len(t)
if c == 0:
    print(s,s)
else:
    if s == 0:
        print(1,c)
        exit()
    print(s,s+c)