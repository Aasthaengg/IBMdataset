n, x = map(int, input().split())
l = [int(i) for i in input().split()]
d, cnt = 0, 1
for li in l:
    d += li
    if d <= x:
        cnt += 1
print(cnt)