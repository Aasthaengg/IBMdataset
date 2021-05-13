n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


count = 0
for i in range(n):
    count += min(a[i],b[i])
    if a[i] < b[i]:
        if  a[i+1] <= (b[i] - a[i]):
            count += a[i+1]
            a[i+1] = 0
        else:
            count += (b[i] - a[i])
            a[i+1] = a[i+1] - (b[i] - a[i])

print(count)