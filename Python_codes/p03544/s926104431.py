n = int(input())

def luc(x):
    x1 = 2
    x2 = 1
    if x == 1:
        return x1
    elif x == 2:
        return x2
    else:
        for i in range(x-2):
            x1,x2 = x2, x1 + x2
        return x2

print(luc(n+1))