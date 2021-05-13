a = list(map(int, input().split()))
k = int(input())
count = 0

while a[1] <= a[0]:
    a[1] = a[1]*2
    count += 1
while a[2] <= a[1]:
    a[2] = a[2]*2
    count += 1

if count > k:
    print('No')
else:
    print('Yes')
