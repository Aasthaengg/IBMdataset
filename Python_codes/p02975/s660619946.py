n = int(input())
a = list(map(int,input().split()))
l = list(set(a))
n = len(l)
if n == 3:
    if l[0] ^ l[1] ^ l[2] == 0:
        x = a.count(l[0])
        y = a.count(l[1])
        z = a.count(l[2])
        if x == y == z:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
elif n == 2:
    z = -1
    if l[0] == 0:
        x = 1
        z = 0
    if l[1] == 0:
        x = 0
        z = 1
    if z != -1:
        x = a.count(l[x])
        z = a.count(l[z])
        if x == z + z:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
elif n == 1:
    if l[0] == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')