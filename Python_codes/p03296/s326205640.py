# -*- coding: utf-8 -*-
n = int(input())
a = [int(i) for i in input().split()]

ans = 0
count = [0 for _ in range(n)]
j = 0
for i in range(n - 1):
    if a[i] == a[i + 1]:
        count[j] += 1
    if a[i] != a[i + 1]:
        count[j] += 1
        j += 1
count[j] += 1
#print(count)

for i in count:
    ans += i // 2
print(ans)
