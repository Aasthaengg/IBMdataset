n = int(input())
a = list(map(int, input().split()))
xor = 0
total = 0
cur = 0
cnt = 0
for i in range(n):
    xor = xor ^ a[i]
    total += a[i]
    if xor != total:
        while True:
            total -= a[cur]
            xor = xor ^ a[cur]
            cur += 1
            if total == xor:
                break
    cnt += (i - cur + 1)
print(cnt)
