data=list(map(int,input().split()))
data.sort()
a=data[0]
b=data[1]
c=data[2]
if a == b == c:
    print(0)
elif b == c:
    count=0
    while a < c:
        a += 2
        count += 1
    if a > c:
        print(count+1)
    else:
        print(count)
else:
    count=0
    while a < c and b < c:
        a += 1
        b += 1
        count += 1
    if a == b == c:
        print(count)
    else:
        while a < c:
            a += 2
            count += 1
        if a > c:
            print(count+1)
        else:
            print(count)