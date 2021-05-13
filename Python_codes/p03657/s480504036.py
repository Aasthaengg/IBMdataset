a, b = map(int, input().split())
print('Possible' if (a%3)*(b%3)*((a+b)%3)==0 else 'Impossible')