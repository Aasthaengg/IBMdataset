n = int(input())
a = list(map(int, input().split()))

max_a = max(a)
min_a = min(a)
count = 0
ans = []
if abs(min_a) <= abs(max_a):
    max_i = 0
    for i in range(n):
        if a[i] == max_a:
            max_i = i
    for i in range(n):
        ans.append([max_i+1, i+1])
        count += 1
    for i in range(n-1):
        ans.append([i+1, i+2])
        count += 1
else:
    min_i = 0
    for i in range(n):
        if a[i] == min_a:
            min_i = i
    for i in range(n):
        ans.append([min_i+1, i+1])
        count += 1
    for i in range(n-1, 0, -1):
        ans.append([i+1, i])
        count += 1

print(count)
for i in ans:
    print(*i)
