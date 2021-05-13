n, c, k = map(int, input().split())
t = [int(input()) for i in range(n)]
t.sort()
cnt = 1
buss = 0
fir = t[0]
for i in range(1, n):
    if fir <= t[i] and t[i] <= fir + k and cnt < c:
        cnt += 1
    else:
        buss += 1
        cnt = 1
        fir = t[i]
if cnt >= 1:
    buss += 1
print(buss)