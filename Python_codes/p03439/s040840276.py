import sys

N = int(input())
p2 = [pow(2,i) for i in range(17) if pow(2,i) <= (N-1)]
m = max(p2)
print('0\n')
s = input()
if s == 'Vacant':
    sys.exit()
elif s == 'Male':
    search = 'F'
else:
    search = 'M'
print('{}\n'.format(m))
s = input()
if s == 'Vacant':
    sys.exit()
elif s == 'Male':
    if search == 'M':
        left = 0
        right = m
    else:
        right = N-1
        left = N-1-m
        print('{}\n'.format(right))
        s = input()
        if s == 'Vacant':
            sys.exit()
        elif s == 'Male':
            search = 'rF'
        else:
            search = 'rM'
else:
    if search == 'F':
        left = 0
        right = m
    else:
        right = N-1
        left = N-1-m
        print('{}\n'.format(right))
        s = input()
        if s == 'Vacant':
            sys.exit()
        elif s == 'Male':
            search = 'rF'
        else:
            search = 'rM'
while True:
    mid = (left+right) // 2
    print('{}\n'.format(mid))
    s = input()
    if s == 'Vacant':
        sys.exit()
    elif s == 'Male':
        if search == 'M':
            right = mid
        elif search == 'rF':
            right = mid
        elif search == 'rM':
            left = mid
        else:
            left = mid
    else:
        if search == 'F':
            right = mid
        elif search == 'rF':
            left = mid
        elif search == 'rM':
            right = mid
        else:
            left = mid