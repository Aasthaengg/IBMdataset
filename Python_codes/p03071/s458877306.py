a, b = map(int, input().split())
l = [a, b, a - 1, b - 1]
l.sort()
print(l[3] + l[2])
