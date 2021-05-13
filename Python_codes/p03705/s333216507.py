n,a,b = [int(x) for x in input().split()]

if a > b:
    print(0)
elif n == 1:
    if a != b:
        print(0)
    else:
        print(1)
else:
    print((b-a)*(n-2)+1)