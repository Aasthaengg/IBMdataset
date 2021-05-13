N, x = map(int, input().split())
*A, = map(int, input().split())
A.sort()
sun = 0
cnt = 0
for a in A:
    if sun + a > x:
        break
    sun += a
    cnt += 1
else:
    if sun < x:
        cnt = max(0, cnt-1)
print(cnt)
