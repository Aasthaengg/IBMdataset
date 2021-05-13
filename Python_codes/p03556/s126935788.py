n = int(input())
cnt = 1
ans = 0
while 1:
    tmp = cnt ** 2
    if tmp <= n:
        ans = tmp
        cnt += 1
    else:
        break

print(ans)
