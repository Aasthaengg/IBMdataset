# ABC 052: A – Two Rectangles
a, b, c, d = [int(x) for x in input().split()]
print(a * b if a * b >= c * d else c * d)