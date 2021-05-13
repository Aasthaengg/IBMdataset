N = int(input())
cnt_max = 0
ans = 1

for i in range(1, N + 1):
    cnt = 0
    num = i
    while True:
        if num % 2 == 0:
            cnt += 1
            num /= 2
        else:
            break
    if cnt_max < cnt:
        cnt_max = cnt
        ans = i

print(ans)
