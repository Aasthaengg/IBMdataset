a = int(input())

x = [0] * (a+1)
for xi in range(1,101):
    for yi in range(1,101):
        for zi in range(1,101):
            result = xi**2 + yi**2 + zi**2 + xi*yi + yi*zi + zi*xi
            if result <= a:
                x[result] += 1 
for i in range(1, a+1):
    print(x[i])