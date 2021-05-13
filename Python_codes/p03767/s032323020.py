n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
count = 0
for i in range(n, 3*n, 2):
    count += a[i]
print(count)
