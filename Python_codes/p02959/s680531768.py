n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for i in range(n-1, -1, -1):
    count += min(a[i] + a[i+1], b[i])
    if b[i] > a[i+1]:
        a[i] -= min(b[i] - a[i+1], a[i])
print(count)