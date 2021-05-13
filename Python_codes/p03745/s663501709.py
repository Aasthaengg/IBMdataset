n = int(input())
a = list(map(int, input().split()))

cnt = 1
sa = 0
for i in range(1, n):
    new = a[i] - a[i-1]
    if new * sa < 0:
        cnt += 1
        sa = 0
        continue
    if new != 0:
        sa = new
print(cnt)