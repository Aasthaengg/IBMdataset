a, b = map(int, input().split())
print('Possible' if any(
    [not(a % 3), not(b % 3), not((a+b) % 3)]) else 'Impossible')
