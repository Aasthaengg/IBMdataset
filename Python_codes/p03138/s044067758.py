n, k = map(int, input().split())
aa = list(map(int, input().split()))

ki = 0
while True:
    if 2 ** ki >= k:
        break
    else:
        ki += 1

mask = 0
for i in range(ki, -1, -1):
    b = 1 << i
    cnt = 0
    for a in aa:
        if a & b > 0:
            cnt += 1
    if len(aa) - cnt > cnt:
        if mask | b <= k:
            mask = mask | b

ans = 0
for a in aa:
    ans += a ^ mask
print(ans)
