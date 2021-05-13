a,b = map(int, input().split())
ab = (a+b)/2
if ab.is_integer() == True:
    print(int(ab))
else:
    print('IMPOSSIBLE')