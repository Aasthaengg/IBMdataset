N = int(input())
max_cnt = 0
ans = 0
for n in range(1, N+1):
    cnt = 0
    for div in range(0, 7):
        if n % 2**div == 0:
            cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        ans = n
print(ans)