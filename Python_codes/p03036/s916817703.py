r,d,l = (int(xi) for xi in input().split())


for xi in range(10):
    l = r*l-d
    print(l)
