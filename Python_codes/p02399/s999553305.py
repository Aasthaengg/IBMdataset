print('{0[0]} {0[1]} {0[2]:.6f}'.format(
      (lambda a, b: (a // b, a % b, a / b))(
       *map(int, input().split()))))