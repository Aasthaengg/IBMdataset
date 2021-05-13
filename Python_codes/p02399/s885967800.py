N = list(map(int, input().split(' ')))

syo = N[0] // N[1]
ram = N[0] % N[1]
fN = N[0] / N[1]
print(syo, ram, '%.5f' % (fN))