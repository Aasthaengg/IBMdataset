l = [int(x) for x in input().split()]
total, ashi = l[0], l[1]

if ashi/2 != int(ashi/2):
    print('No')
else:
    if total <= ashi/2:
        if 2*total >= ashi/2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')