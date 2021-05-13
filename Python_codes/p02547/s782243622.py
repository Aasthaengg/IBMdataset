n = int(input())
cnt = 0
is_ok = False
for _ in range(n):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        cnt += 1
    else:
        cnt = 0
    if cnt >= 3:
        is_ok = True
    else:
        pass
if is_ok:
    print('Yes')
else:
    print('No')
