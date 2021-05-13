n, x = map(int, input().split())
l = [int(i) for i in input().split()]
d, cnt = 0, 1
for li in l:
    if d + li <= x:
        d += li
        cnt += 1
    else:
        break
print(cnt)