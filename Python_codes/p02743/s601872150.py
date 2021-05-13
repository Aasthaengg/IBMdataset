# coding: utf-8
a,b,c = list(map(int, input().split()))

is_0 = 4 * a*b - (c-a-b)**2
if (c-a-b) < 0:
    print('No')
elif is_0 < 0:
    print('Yes')
else:
    print('No')