line = input()
A, B = [int(n) for n in line.split()]
print('Yay!' if A <= 8 and B <= 8 else ':(')
