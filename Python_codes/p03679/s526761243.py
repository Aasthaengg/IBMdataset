x, a, b = map(int, input().split())
if a - b >= 0:
    print('delicious')
    exit()
if a - b + x >= 0:
    print('safe')
else:
    print('dangerous')
