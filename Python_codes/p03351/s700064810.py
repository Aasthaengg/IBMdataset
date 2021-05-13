a, b, c, d = map(int,input().split())
flag = 0
if -d <= a - c <= d:
    flag = 1
if -d <= a - b <= d and -d <= b - c <= d:
    flag = 1
if flag:
    print('Yes')
else:
    print('No')