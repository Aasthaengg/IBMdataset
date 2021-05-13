import math

N = int(input())
f = False
for h in range(1,3501):
    if f:
        break
    for n in range(1,3501):
        if 4*n*h-N*n-N*h == 0:
            continue
        check = N*n*h/(4*n*h-N*n-N*h)
        if check < 0:
          continue
        if check.is_integer():
            print(h, n, math.floor(check))
            f = True
            break