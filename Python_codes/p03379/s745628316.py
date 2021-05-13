n = int(input())
x = list(map(int, input().split()))
pivot = n // 2
l = []
for i in range(n):
    l.append([x[i], i])
l.sort()
r = []
for i in range(n):
    l[i].append(i)
    l[i] = l[i][1:]
    r.append([l[i][1], l[i][0]])
d1 = dict(l)
d2 = dict(r)
for i in range(n):
    if d1[i] >= pivot:
        print(x[d2[pivot-1]])
    else:
        print(x[d2[pivot]])