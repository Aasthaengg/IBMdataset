dict = {0: 'Sunny', 1: 'Cloudy', 2: 'Rainy'}
S = input()
for i, k in enumerate(dict.items()):
    if k[1] == S:
        print(dict[(k[0] + 1) % 3])
        exit()
