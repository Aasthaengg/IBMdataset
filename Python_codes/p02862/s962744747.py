X, Y = list(map(int,input().split()))

from functools import reduce

def cmb(n, r):
    INF = 10 ** 9 + 7
    r = min(n - r, r)
    if r == 0:  return 1
    numer = reduce(lambda x, y: (x * y) % INF, range(n, n - r, -1))
    denom = reduce(lambda x, y: (x * y) % INF, range(1, r + 1))
    return (numer * pow(denom, INF - 2, INF)) % INF

temp1 = 2 * X - Y
temp2 = 2 * Y - X
if temp1 % 3 or temp2 % 3:  print(0)
elif temp1 < 0 or temp2 < 0:  print(0)
else:
    a = temp1 // 3
    b = temp2 // 3
    print(cmb(a + b, a))