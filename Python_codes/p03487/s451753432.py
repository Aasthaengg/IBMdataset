n = int(input())
a = list(map(int, input().split()))

cnt = [0] * (n+1)
res = 0
for v in a:
    if v <= n:
        cnt[v] += 1
    else:
        res += 1

for i in range(1, n+1):
    if cnt[i] < i:
        res += cnt[i]
    else:
        res += cnt[i] - i

print(res)