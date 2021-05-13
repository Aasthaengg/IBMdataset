A, B = map(int, input().split())
a = A + B
b = A - B
c = A * B
l = []
l.append(a)
l.append(b)
l.append(c)
l.sort()
print(l[-1])