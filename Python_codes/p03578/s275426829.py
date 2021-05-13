from collections import defaultdict
n = int(input())
d = tuple(map(int, input().split()))
m = int(input())
t = tuple(map(int, input().split()))
l = defaultdict(int)
for x in d:
    l[x] += 1
for y in t:
    if l[y] == 0:
        print('NO')
        exit()
    l[y] -= 1
print('YES')
