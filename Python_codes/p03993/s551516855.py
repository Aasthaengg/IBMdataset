n = int(input())
a = [0] + list(map(int, input().split()))
cnt = 0
for i in range(1, n + 1):
    if i == a[a[i]]:
        cnt += 1
cnt //= 2
print(cnt)
