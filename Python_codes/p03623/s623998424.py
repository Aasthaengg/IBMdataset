x, a, b = map(float,input().split())

if abs(x - a) < abs(x - b):
    print("A")
else:
    print("B")
