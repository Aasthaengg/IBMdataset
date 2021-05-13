A, B = map(int,input().split())
print('Possible' if 0 in [(A+B)%3, A%3, B%3] else 'Impossible')