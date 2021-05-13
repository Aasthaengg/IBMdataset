n = int(input())
a = sorted(list(map(int, input().split())), reverse = True)
l1 = 0
l2 = 0
j = 0
for i in range(n - 1):
    j = i + 1
    if a[i] == a[i + 1]:
        l1 = a[i]
        j = i + 2
        break
for i in range(j, n - 1):
    if a[i] == a[i + 1]:
        l2 = a[i]
        break
print(l1 * l2)
