x = input()

a, b = x.split()
if int(a) == int(b):
    print('a == b')
elif int(a) > int(b):
    print('a > b')
elif int(a) < int(b):
    print('a < b')