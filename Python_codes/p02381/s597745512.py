import sys
 
mode = 0
for line in sys.stdin:
    if mode == 0:
        n = int(line.strip('\n'))
        if n == 0: break
        mode = 1
    elif mode == 1:
        x = [float(i) for i in line.strip('\n').split()]
        ave = sum(x) / n
        std = (sum([(i-ave)**2 for i in x])/n)**0.5
        print std
        mode = 0