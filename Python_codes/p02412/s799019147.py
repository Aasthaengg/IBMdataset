while True:
    n,x = [int(i) for i in input().split()]
    if n == 0 and x == 0: break
    count = 0
    # 3????????°?????????????°????x//3?????????x//3 * 3 == x ?????????????°????x//3??\?????§?????????????????????
    for a in range(1, x//3):
        # 3????????°?????????????????????x//2?????????x//2 * 2 == x ?????????????????????x//2??\?????§?????????????????????
        for b in range(a+1,x//2):
            c = x - (a + b)
            if b < c <= n:
                count += 1
    print(count)