n = int(input())
a = list(map(int, input().split()))
a.sort()
x = a[-1]
y1 = x//2
y2 = x//2 + 1
sa1, sa2 = float("inf"), float("inf")
z1, z2 = 0, 0
for i in range(n-1):
    if sa1 > abs(y1 - a[i]):
        sa1 = abs(y1-a[i])
        z1 = a[i]
    if sa2 > abs(y2 - a[i]):
        sa2 = abs(y2 - a[i])
        z2 = a[i]

if sa1 > sa2:
    print(x, z2)
else:
    print(x, z1)


