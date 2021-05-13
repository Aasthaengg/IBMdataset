list_XY = input().split()
list_XY_sorted = sorted(list_XY)

if list_XY[0] == list_XY[1]:
    print('=')
elif list_XY == list_XY_sorted:
    print('<')
else:
    print('>')