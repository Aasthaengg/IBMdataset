O = input()
E = input()

if len(O) == len(E):
    for i in range(len(O)):
        print(O[i], end='')
        print(E[i], end='')
    print('')
else:
    for i in range(len(E)):
        print(O[i], end='')
        print(E[i], end='')
    print(O[-1])