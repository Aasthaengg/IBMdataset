x, a, b = map(int, input().split())

if a-b >= 0:
    print("delicious")

if a-b < 0:
    if b-a <= x:
        print('safe')
if b > x+a:
    print("dangerous")
