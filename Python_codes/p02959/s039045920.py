n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for i in range(n):
    count += min(a[i], b[i])
    b[i] = max(b[i]-a[i], 0)

    count += min(a[i+1], b[i])
    a[i+1] = max(a[i+1] - b[i], 0)

print(count)
