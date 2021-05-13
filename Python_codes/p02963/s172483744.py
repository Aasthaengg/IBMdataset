s = int(input())

x1, x2, x3 = 0, 10 ** 9, 1
a = -(-s // (10 ** 9))
b = a * (10 ** 9) - s

y1, y2, y3 = 0, b, a

print(x1, y1, x2, y2, x3, y3)


#print(abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)))