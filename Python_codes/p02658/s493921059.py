n = int(input())
a = [int(v) for v in input().split()]
limit = 1000000000000000000
if 0 in a:
    print (0)
else:
    ans = 1
    num = 1
    for i in a:
        num *= i
        if num > limit:
            num = -1
            break
    ans = num
    print(ans)