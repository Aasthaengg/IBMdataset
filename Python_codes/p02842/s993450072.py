from math import floor
N = int(input())
Flag = False
for X in range(1,46300):
    if floor(X*1.08)==N:
        Flag = True
        break
print([':(',X][Flag])