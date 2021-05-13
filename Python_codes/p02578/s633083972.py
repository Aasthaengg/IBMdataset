n = int(input())
a = list(map(int,input().split()))

hight_sum = 0
for i in range(n-1):
    hight = 0
    diff = a[i+1] - a[i]
    if diff < 0:
        hight -= diff
        a[i+1] -= diff
        hight_sum += hight
print(hight_sum)