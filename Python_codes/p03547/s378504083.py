x, y = input().split()
shinsu = {
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6
}

if shinsu[x] < shinsu[y]:
    print('<')
elif shinsu[x] > shinsu[y]:
    print('>')
else:
    print('=')