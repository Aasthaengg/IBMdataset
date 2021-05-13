x = input()
N = int(x)

if N % 10 == 2 or N % 10 == 4 or N % 10 == 5 or N % 10 == 7 or N % 10 == 9:
    print('hon')
elif N % 10 == 3:
    print('bon')
else:
    print('pon')