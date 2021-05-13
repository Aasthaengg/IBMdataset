a, b, c, d = map(int, input().split())
if abs(a-c) <= d:
    print('Yes')
    exit()
l = [a, b, c]
l.sort()
if l[2] - l[1] <= d and l[1] - l[0] <= d:
    print("Yes")
else:
    print('No')