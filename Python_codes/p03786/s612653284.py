n = int(input())
a = sorted(list(map(int,input().split())))
cur = a[0]
count = 1
for i in range(1,n):
    if a[i] <= cur*2:
        count += 1
    else:
        count = 1
    cur += a[i]
print(count)