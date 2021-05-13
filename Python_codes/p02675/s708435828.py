n = int(input()) % 10

h = [2, 4, 5, 7, 9]
p = [0, 1, 6, 8]
b = [3]

if n in h:
    print('hon')
elif n in p:
    print('pon')
else:
    print('bon')