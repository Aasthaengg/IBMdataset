n = int(input())
a = list(map(int, input().split()))
ans = 0
skip = False
for i in range(1, n):
    if skip:
        skip = False
        continue
    if a[i-1] == a[i]:
        ans += 1
        skip = True
print(ans)
