a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

c = abs(a - b)
d = (v - w) * t

if c <= d:
    print('YES')
else:
    print('NO')
