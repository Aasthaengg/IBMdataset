n = int(input())
a = [int(x) for x in input().split()]

cnt = 0
for i in range(n):
    if a[i] < 0:
        cnt += 1
        a[i] *= -1

a.sort()

if cnt % 2 != 0:
    a[0] *= -1

print(sum(a))