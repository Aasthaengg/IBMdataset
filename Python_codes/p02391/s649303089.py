ab = input()
num_ab = ab.split()
a = int(num_ab[0])
b = int(num_ab[1])
if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')