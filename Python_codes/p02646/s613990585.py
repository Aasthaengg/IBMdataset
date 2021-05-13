a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if v <= w:
    print('NO')
else:
    if -1 < ((b - a) / (v - w)) < 1:
        print('NO')
    elif 1 <= (abs(b - a) / (v - w)) <= t:
        print('YES')
    else:
        print('NO')