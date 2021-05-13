r,D,x = (int(x) for x in input().split())
Disp = [0]*11
Disp[0] = x
for T in range(0,10):
    Disp[T+1] = r*Disp[T]-D
print('\n'.join(str(x) for x in Disp[1:]))