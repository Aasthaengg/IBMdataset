n = int(input())
a = [int(n) for n in input().split(' ')]

if 0 in a:
    print(0)
else:
    mul = 1
    for ai in a:
        mul *= ai
        if mul > 10**18:
            mul = -1
            break
    print(mul)
