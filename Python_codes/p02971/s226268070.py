n = int(input())
alist = []
for i in range(n):
    a = int(input())
    alist.append(a)
aalist = sorted(alist)
ans = 0
for i in range(n):
    ans = aalist[-1]
    if alist[i] == aalist[-1]:
        ans = aalist[-2]
    print(ans)
