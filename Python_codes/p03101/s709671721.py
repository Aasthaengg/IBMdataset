a, b = (int(i) for i in input().split())
c, d = (int(i) for i in input().split())

print(a*b - b*c - a*d + c*d)