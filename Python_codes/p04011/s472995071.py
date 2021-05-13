x = []
for i in range(4):
    x.append(int(input()))
if x[0] > x[1]:
    print(x[1]*x[2]+(x[0]-x[1])*x[3])
else:
    print(x[0]*x[2])