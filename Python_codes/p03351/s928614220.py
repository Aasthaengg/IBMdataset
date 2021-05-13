a, b, c, d = map(int, input().split())
d_ab = b - a
d_bc = c - b
d_ac = c - a
if d_ab <0:
    d_ab = a - b
if d_bc <0:
    d_bc = b - c
if d_ac <0:
    d_ac = a - c

if (1 <= a & a <= 100) & (1 <= b & b <= 100) & (1 <= c & c <= 100) & (1 <= d & d <= 100):
    if 0 <= d_ac & d_ac <= d:
        print('Yes')
    elif (0 <= d_ab & d_ab <= d) & (0 <= d_bc & d_bc <= d):
        print('Yes')
    else:
        print('No')
else:
    print('No')