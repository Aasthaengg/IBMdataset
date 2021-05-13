n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for x in range(1,n):
        tmp = (1+x)*x//2
        if tmp >= n:
            l = x
            break

    d = tmp - n
    for x in range(1,l+1):
        if x != d:
            print(x)