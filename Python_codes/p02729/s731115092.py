a = list(map(int, input().split()))
n = a[0]
m = a[1]
print((m+n)*(m+n-1) // 2 - m * n)