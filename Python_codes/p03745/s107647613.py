n = int(input())
a = list(map(int,input().split()))
sw = 0
count = 1
for i in range(n-1):
    if sw == 1:
        if a[i+1]<a[i]:
            sw = 0
            count += 1
    elif sw == -1:
        if a[i+1]>a[i]:
            sw = 0
            count += 1
    else:
        if a[i+1]>a[i]:
            sw = 1
        elif a[i]>a[i+1]:
            sw = -1
print(count)