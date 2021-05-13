a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
 
if a < b:
    if v <= w:
        print('NO')
    else:
        if b - a <= t * (v - w):
            print('YES')
        else:
            print('NO')
elif a > b:
    if v <= w:
        print('NO')
    else:
        if a - b <= t * (v - w):
            print('YES')
        else:
            print('NO')