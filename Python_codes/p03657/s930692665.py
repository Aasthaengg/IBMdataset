A, B = map(int,input().split())
list = [(A+B)%3, A%3, B%3]
print('Possible' if 0 in list else 'Impossible')