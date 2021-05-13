a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if a-v*t <= b-w*t and b+w*t <= a+v*t:
    print('YES')
else:
    print('NO')