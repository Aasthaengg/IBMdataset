r, D, x = [int(n) for n in input().split()]
y =[x]
for i in range(10):
    y.append(r*y[i]-D)
    print(y[i+1])
