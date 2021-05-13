def gap(a,b):
    x = b-a
    if x<0:
        x = 10**18
    return x

a,b = [int(i) for i in input().split()]
print(min(gap(a,b), 1+gap(a,-b), 1+gap(-a,b), 2+gap(-a,-b)))