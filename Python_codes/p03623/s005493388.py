x, a, b = map(int, input().split())
da = abs(x-a)
db = abs(x-b)
if da < db:
    print('A')
elif db < da:
    print('B')