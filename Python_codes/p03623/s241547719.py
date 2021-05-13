x,a,b = map(int, input().split())
xa = (x-a)**2
xb = (x-b)**2

if xa > xb:
    print('B')
elif xb > xa:
    print('A')