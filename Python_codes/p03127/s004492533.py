n = int(input())
a = list(map(int, input().split()))

while True:
    m = min(a)
    for i in range(len(a)):
        if a[i] != m:
            a[i] = a[i] % m
    a.sort()
    z = a.count(0)
    a = a[z:]
    if min(a) == m:
        break
print(m)
