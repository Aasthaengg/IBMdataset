n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i, e in enumerate(a, 1):
    if a[e-1] == i:
        cnt += 1

cnt //= 2
print(cnt)
