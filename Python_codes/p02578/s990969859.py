n = int(input())
a = list(map(int, input().split()))
count = 0
i = 1
while i < len(a):
    if a[i] < a[i-1]:
        count += a[i-1] - a[i]
        a[i] = a[i-1]
    i += 1
print(count)