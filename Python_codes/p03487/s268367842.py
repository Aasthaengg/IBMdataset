from _collections import defaultdict
n = int(input())
a = list(map(int,input().split()))
a_max = max(a)
l = defaultdict(int)
count = 0
for i in range(n):
    l[a[i]] += 1
    count += 1
    if l[a[i]] == a[i]:
        count -= a[i]
print(count)