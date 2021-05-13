n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
cnt = 0
for i in range(n):
    dm = min(a[i], b[i])
    b[i] -= dm; cnt += dm
    dmn = min(a[i + 1], b[i])
    a[i + 1] -= dmn; cnt += dmn
print(cnt)