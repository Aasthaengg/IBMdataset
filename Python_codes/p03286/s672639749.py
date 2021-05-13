N = int(input())

if N == 0:
    print(0)
else:
    ret = ""
    while N != 0:
        if N % 2 != 0:
            N -= 1
            ret = "1" + ret
        else:
            ret = "0" + ret
        N //= -2
    print(ret)
