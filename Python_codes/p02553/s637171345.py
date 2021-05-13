a, b, c, d = map(int, input().split())
L = [a*c, b*c, a*d, b*d]
L.sort()
print(L[3])