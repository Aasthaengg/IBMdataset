N = input()

n = int(list(N)[-1])
if n == 0 or n == 1 or n == 6 or n == 8: print('pon')
elif n == 3: print('bon')
else: print('hon')