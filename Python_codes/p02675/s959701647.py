N = int(input())

h = [2, 4, 5, 7, 9]
p = [0, 1, 6, 8]
b = [3]

NN = N % 10
if NN in h:
    print('hon')
elif NN in p:
    print('pon')
else:
    print('bon')

