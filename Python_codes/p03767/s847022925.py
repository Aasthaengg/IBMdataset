n = int(input()); a = list(map(int, input().split()))
a.sort(); x = 0
for i in range(n, 3*n-1, 2): x += a[i]
print(x)