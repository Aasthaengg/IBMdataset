x = [int(input()) for i in range(4)]
if x[0]<x[1]:
    print(x[0]*x[2])
else:
    print(x[1]*x[2]+(x[0]-x[1])*x[3])