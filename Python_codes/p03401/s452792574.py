n = int(input())
a = [0]
for i in list(map(int, input().split())):
    a.append(i)
a.append(0)

cost = 0
for i in range(len(a) - 1):
    cost += abs(a[i] - a[i + 1])

for i in range(1, n + 1):
    if a[i - 1] <= a[i] <= a[i + 1] or a[i - 1] >= a[i] >= a[i + 1]:
        print(cost)
    else:
        dec = abs(a[i] - a[i - 1]) + abs(a[i + 1] - a[i])
        inc = abs(a[i + 1] - a[i - 1])
        print(cost - dec + inc)
