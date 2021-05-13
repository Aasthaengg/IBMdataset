A,B = map(int,input().split())
print('Possible' if any([True if val%3==0 else False for val in [A,B,A+B]]) else 'Impossible')