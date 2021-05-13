S = input()

ones = S.count('1')
zeros = S.count('0')
print(min(ones, zeros) * 2)