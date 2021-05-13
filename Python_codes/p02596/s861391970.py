k = int(input())
x = 7%k
cnt = 0

if k%2 ==0:
    print('-1')
else:
    while True:
        cnt += 1
        if x == 0:
            print(cnt)
            break
        elif cnt == k:
            print('-1')
            break
        else:
            x = (x*10+7)%k