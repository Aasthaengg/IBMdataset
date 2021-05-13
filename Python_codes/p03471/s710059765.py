N,Y  = (int(T) for T in input().split())
Flag = False
for Y10 in range(0,N+1):
    for Y5 in range(0,N+1-Y10):
        Y1 = N-(Y10+Y5)
        if 10*Y10+5*Y5+Y1==Y//1000:
            Flag = True
            Disp = [str(T) for T in [Y10,Y5,Y1]]
            break
    if Flag:
        break
if Flag:
    print(' '.join(Disp))
else:
    print('-1 -1 -1')