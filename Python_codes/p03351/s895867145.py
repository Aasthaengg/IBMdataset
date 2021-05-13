a,b,c,d = map(int, input().split())
y = 0
if abs(a-b) <= d:
    if abs(b-c) <= d:
        y = 1
else:
    if abs(a-c) <= d:
        y = 1
if y == 1:
    print('Yes')
else:
    print('No')