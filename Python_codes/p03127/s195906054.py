n = int(input())
a = list(map(int, input().split()))

m = 0
tmp = min(a)
while m != tmp:
    m = tmp
    for i in range(n):
        if a[i] != m:
            a[i] = a[i] % m
        if a[i] < m and a[i] != 0:
            tmp = a[i]
print(m)
