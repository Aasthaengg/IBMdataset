n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
acsum = [0]

for i in range(n):
    acsum.append(acsum[i] + a[i])

if acsum[-1] < x:
    print(n - 1)
else:
    for i in range(n + 1):
        if acsum[i] == x:
            print(i)
            break
        if acsum[i] > x:
            print(i - 1)
            break