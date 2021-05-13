import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
ans = []

max_a = [-float('inf'), 100]
min_a = [float('inf'), 100]

for i in range(n):
    if a[i] >= max_a[0]:
        max_a = [a[i], i]
    if a[i] <= min_a[0]:
        min_a = [a[i], i]

if abs(max_a[0]) >= abs(min_a[0]):
    for i in range(n):
        if i != max_a[1]:
            a[i] += max_a[0]
            ans.append([max_a[1], i])
    for i in range(1, n):
        if a[i] < a[i - 1]:
            a[i] += a[i - 1]
            ans.append([i - 1, i])
else:
    for i in range(n):
        if i != min_a[1]:
            a[i] += min_a[0]
            ans.append([min_a[1], i])
    for i in range(n - 1, 0, -1):
        if a[i] < a[i - 1]:
            a[i - 1] += a[i]
            ans.append([i, i - 1])
print(len(ans))
for i in ans:
    x, y = i
    print(x + 1, y + 1)




