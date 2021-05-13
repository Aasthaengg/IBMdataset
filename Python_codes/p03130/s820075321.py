import collections
a1,b1 = list(map(int,input().split()))
a2,b2 = list(map(int,input().split()))
a3,b3 = list(map(int,input().split()))
dd = collections.defaultdict(int)
dd[a1] += 1
dd[a2] += 1
dd[a3] += 1
dd[b1] += 1
dd[b2] += 1
dd[b3] += 1
for i in dd.values():
    if i > 2:
        print('NO')
        exit()
print('YES')