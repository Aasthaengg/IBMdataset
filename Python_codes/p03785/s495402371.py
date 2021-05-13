N, C, K = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))

a.sort()
ans = 1
count = 0
pre = a[0]
for i in range(N):
    if count == 0:
        pre = a[i]
    if count >= C or a[i]-pre > K:
        count = 0
        ans += 1
        pre = a[i]
    count += 1
print(ans)
