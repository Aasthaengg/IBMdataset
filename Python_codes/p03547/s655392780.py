x, y = map(str, input().split())
if x == y:
    print('=')
elif int(x, 16) > int(y, 16):
    print('>')
else:
    print('<')