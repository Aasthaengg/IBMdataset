N = int(input())
m = 1
d_cnt = 0
for i in range(1, N+1):
    num = i
    cnt = 0
    while True:
        if num % 2 == 0:
            num /= 2
            cnt += 1
        else:
            break
    if d_cnt < cnt:
        d_cnt = cnt
        m = int(i)
print(m)