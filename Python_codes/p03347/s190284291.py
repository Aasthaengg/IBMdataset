n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

if a[0] > 0:
    print(-1)
    exit()

for i in range(1, n):
    if a[i] > i:
        print(-1)
        exit()
    if a[i] > a[i - 1] + 1:
        print(-1)
        exit()

if n == 1:
    print(0)
    exit()

result = 0

if a[n-1] != 0:
    result += a[n-1]

for i in range(2, n):
    j = n - i
    if a[j] != 0 and a[j] != a[j + 1] - 1:
            result += a[j]

print(result)