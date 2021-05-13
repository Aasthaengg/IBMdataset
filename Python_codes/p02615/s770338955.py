from sys import stdin
n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
a.sort(reverse = True)
ans = a[0]
count = 0
cur = 1
for _ in range(n-2):
    ans += a[cur]
    count += 1
    if count == 2:
        count = 0
        cur += 1
print(ans)
