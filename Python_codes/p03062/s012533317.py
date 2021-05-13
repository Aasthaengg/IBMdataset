n = int(input())
a = list(map(int, input().split()))

min_abs = float('inf')
cnt = 0
for i in range(n):
    if a[i] < 0:
        cnt += 1
        a[i] *= -1
    min_abs = min(min_abs, a[i])

if cnt % 2 == 0:
    print(sum(a))
else:
    print(sum(a) - 2 * min_abs)