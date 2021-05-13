n = int(input())
lists = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        lists[i].append((x-1, y))
ans = 0
for i in range(1, 2**n):
    status = True
    for j in range(n):
        if (i >> j) & 1 == 0:
            continue
        for x, y in lists[j]:
            if (i >> x) & 1 != y:
                status = False
                break
        if status == False:
            break
    if status == True:
        ans = max(ans, bin(i).count('1'))
print(ans)