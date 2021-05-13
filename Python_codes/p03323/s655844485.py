line = input()

a, b = [int(n) for n in line.split()]

if a <= 8 and b <=8:
    print('Yay!')
else:
    print(':(')