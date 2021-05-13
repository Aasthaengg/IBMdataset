x, y = map(int, input().split())

if x%y == 0:
    ans = -1
else:
    ans = 0
    cnt = 2
    while True:
        if (x*cnt)%y != 0:
            ans = x*cnt
            break
        else:
            cnt += 1

print(ans)