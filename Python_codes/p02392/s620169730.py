a, b, c = input().split()
check1 = int(b) - int(a)
check2 = int(c) - int(b)
if check1 > 0 and check2 > 0:
    print('Yes')
else:
    print('No')