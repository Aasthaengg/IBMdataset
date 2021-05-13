n = int(input())
a = list(map(int, input().split()))

cnt = n
prev = a[0]
trend ='N'

for i in range(1, n):
    if a[i] > prev:
        if (trend == 'U' or trend == 'N'):
            cnt -= 1
            trend ='U'
        else:
            trend = 'N'
    if a[i] < prev:
        if (trend == 'D' or trend == 'N'):
            cnt -= 1
            trend = 'D'
        else:
            trend = 'N'
    if a[i] == prev:
        cnt -= 1
    prev = a[i]
print(cnt)