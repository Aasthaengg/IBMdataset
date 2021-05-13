level = 0
x, a, b = map(int, input().split())
level -= a
level += b
if a - b >= 0:
    print('delicious')
elif b - a <=  x:
    print('safe')
else:
    print('dangerous')
