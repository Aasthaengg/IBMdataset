n = int(input())
As = [int(num) for num in input().split()]

As_sorted = sorted(As, reverse=True)
if As_sorted[-1] == 0:
    print(0)
else:
    flag = False
    res = 1
    for num in As_sorted:
        res *= num
        if res > 10**18:
            flag = True
            break            
    if flag:
        print(-1)
    else:
        print(res)