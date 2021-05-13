a, b, c, d = map(int, input().split())

check = False
if abs(a-c) <= d:
    check = True
else:
    if abs(a-b) <= d and abs(b-c) <= d:
        check = True

if check:
    print('Yes')
else:
    print('No')