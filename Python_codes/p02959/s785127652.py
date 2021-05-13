n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
total = 0
cnt = 0
total_l = []
cnt_l = []
for i in range(n):
    if a[i] - (b[i] - cnt) >= 0:
        total += b[i] - cnt
        cnt = 0
    else:
        total += a[i]
        cnt = max(-b[i], a[i] - (b[i] - cnt))

if cnt < 0:
    total += min(a[n], abs(cnt))

print(total)