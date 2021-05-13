n = int(input())
a = list(map(int, input().split()))
ans = 0
prev = a[0]
for i in range(1, n):
    if a[i] == prev:
        ans += 1
        prev = -1
    else:
        prev = a[i]
print(ans)