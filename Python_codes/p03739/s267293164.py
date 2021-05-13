n = int(input())
a = list(map(int,input().split()))
SUM = 0
cnt = 0
for i in range(n):
    SUM += a[i]
    if i % 2 == 0:
        cnt += max(0, 1 - SUM)
        SUM = max(1, SUM)
    else:
        cnt += max(0, 1 + SUM)
        SUM = min(-1, SUM)
ans = cnt

SUM = 0
cnt = 0
for i in range(n):
    SUM += a[i]
    if i % 2 == 0:
        cnt += max(0, 1 + SUM)
        SUM = min(-1, SUM)
    else:
        cnt += max(0, 1 - SUM)
        SUM = max(1, SUM)
ans = min(ans, cnt)
print(ans)