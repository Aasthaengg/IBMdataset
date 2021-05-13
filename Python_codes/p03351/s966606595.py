a, b, c, d = map(int, input().split())

flag = 0
if abs(a-c) <= d:
    flag = 1
elif abs(a-b) <= d and abs(c-b) <= d:
    flag = 1

if flag:
    print('Yes')
else:
    print('No')