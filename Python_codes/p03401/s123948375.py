n = int(input())
a = list(map(int, input().split()))

total = abs(a[0]) + abs(a[n - 1])
for i in range(1, n):
    total += abs(a[i] - a[i - 1])

def calc(a, i, total):
    if i == 0:
        pre = 0
    else:
        pre = a[i - 1]

    if i != len(a) - 1:
        return total - (abs(a[i] - pre) + abs(a[i] - a[i + 1])) + abs(pre - a[i + 1])
    else:
        return total - (abs(pre - a[i]) + abs(a[i])) + abs(pre)

for i in range(n):
    print(calc(a, i, total))