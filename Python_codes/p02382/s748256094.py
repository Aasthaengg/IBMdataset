def minkowski(n, x, y, p):
    D = 0
    for i in range(n):
        D += abs(x[i] - y[i])**p

    return(D**(1/p))

def chebyshev(n, x, y):
    D = []
    for i in range(n):
        D.append(abs(x[i] - y[i]))

    return(max(D))

n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

print(minkowski(n, x, y, 1))
print(minkowski(n, x, y, 2))
print(minkowski(n, x, y, 3))

print(chebyshev(n, x, y))