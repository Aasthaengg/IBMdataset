def mass(r, D, x):
    return r*x - D


r, D, x = map(int, input().split())
for _ in range(10):
    x = mass(r, D, x)
    print(x)