a,b = map(int,input().split())
if a == b:
    print(0)
if int((a+b)/2) == (a+b)/2:
    print(int((a+b)/2))
else:
    print('IMPOSSIBLE')