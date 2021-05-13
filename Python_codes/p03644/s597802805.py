N = int(input())
cnt_max = 0

for i in range(N):
    num = i+1
    cnt = 0
    while True :
        if num % 2 == 0:
            cnt += 1
            num /= 2
        else:
            break
    if cnt_max < cnt:
        cnt_max = cnt

print(2**cnt_max)