n = int(input())
a = [int(x) for x in input().split()]
ans = 'No'
for i in range(n):
    if a[i] % 4 == 0:
        a[i] = 4
    elif a[i] % 2 == 0:
        a[i] = 2
    else:
        a[i] = 1

if a.count(2) != 0:
    if a.count(4) >= a.count(1):
        ans = 'Yes'
else:
    if a.count(4) + 1 >= a.count(1):
        ans = 'Yes'
print(ans)
