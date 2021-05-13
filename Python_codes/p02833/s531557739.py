n = int(input())

if n%2==1:
    print(0)
else:
    # 2の倍数には不足しないので、5の倍数を数える
    cnt=0
    n //= 2
    while n:
        n //= 5
        cnt += n
    print(cnt)