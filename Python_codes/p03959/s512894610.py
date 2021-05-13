n = int(raw_input())
t = map(int, raw_input().split())
a = map(int, raw_input().split())
mi = [1 for i in range(n)]
ma = [10**9 for i in range(n)]
for i, e in enumerate(t):
    if i == 0:
        mi[i] = e
        ma[i] = e
    else:
        if e > t[i-1]:
            mi[i] = e
            ma[i] = e
        elif e == t[i-1]:
            ma[i] = e
        else:
            print 0
            exit()

a = a[::-1]
mi = mi[::-1]
ma = ma[::-1]

for i, e in enumerate(a):
    if i == 0:
        if mi[i] <= e <= ma[i]:
            mi[i] = e
            ma[i] = e
        else:
            print 0
            exit()
    else:
        if e > a[i-1]:
            if mi[i] <= e <= ma[i]:
                mi[i] = e
                ma[i] = e
            else:
                print 0
                exit()
        elif e == a[i-1]:
            if mi[i] <= e <= ma[i]:
                ma[i] = e
        else:
            print 0
            exit()
res = 1
for i in range(n):
    res *= ma[i] - mi[i] + 1
    res = res % (10**9+7)
print res % (10**9+7)
