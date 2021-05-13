a, b, c, k = map(int, input().split())

cnt = 0
if k > a:
    cnt += a
    if k-a > b:
        if k-a-b > 0:
            cnt -= k-a-b
else:
    cnt += k

print(cnt)