n = int(raw_input())
a = map(int, raw_input().split())

count = 0
for i in range(n):
    minj = i
    for j in range(i, n):
        if a[j] < a[minj]:
            minj = j
            
    if a[i] != a[minj]:
        tmp = a[i]
        a[i] = a[minj]
        a[minj] = tmp
        count += 1

for i in range(n):
    if i == n-1:
        print a[i]
    else:
        print a[i],

print count