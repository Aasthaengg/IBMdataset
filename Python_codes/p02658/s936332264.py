N = int(input())
A = [int(x) for x in input().split()]
sum = 1
big = False
if 0 in A:
    print(0)
else:
    for a in A:
        sum *= a
        if sum > 10**18:
            big = True
            break
    if big:
        print(-1)
    else:
        print(sum)