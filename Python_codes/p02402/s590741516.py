n = int(input())
a = list(map(int, input().split()))
minimum = 1000001
maximum = -1000001
sum = 0
for i in range(n):
    if(a[i] < minimum):
        minimum = a[i]
    if(maximum < a[i]):
        maximum = a[i]
    sum += a[i]
print("%d %d %d" % (minimum, maximum, sum))