A, B = [int(i) for i in input().split()]
print('Possible' if True in (A % 3 == 0, B % 3 == 0, (A + B) % 3 == 0) else 'Impossible')