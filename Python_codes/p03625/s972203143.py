n = int(input())
a = list(map(int,input().split()))

adic = {}
for i in range(n):
    if a[i] not in adic:
        adic[a[i]] = 0
    adic[a[i]] += 1

alist = sorted(adic.items(),reverse = True)
before = 0
after = 0

for i in range(len(alist)):
    if before == 0:
        if alist[i][1] >= 4:
            before = alist[i][0]
            after = alist[i][0]
            break
        elif alist[i][1] >= 2:
            before = alist[i][0]
    else:
        if alist[i][1] >= 2:
            after = alist[i][0]
            break
print(before * after)


