n = int(input())
a = list(map(int, input().split()))
mul = 1
flag = 0
if 0 in a:
    flag = 2
    print(0)
else:
    for i in range(n):
        mul = mul * a[i]
        if mul > 10**18:
            print(-1)
            flag = 1
            break
if flag == 0:
    print(mul)