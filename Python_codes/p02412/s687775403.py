while True:
    n,x = map(int,input().split())
    if n == x == 0: break
    ret = 0
    max = x - 2

    if n <= x: max = n  
    for _ in range(max):
        if max == 2: break
        mid = max - 1
        for _ in range(mid):
            min = x - max - mid

            if min <= 0: mid -= 1
            elif min >= mid:

                break
            else: 
                ret += 1
                mid -= 1
        max -= 1
    print(ret)