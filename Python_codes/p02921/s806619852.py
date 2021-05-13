s = list(input())
t = list(input())
a = zip(s, t)

b = list(map(lambda xy: xy[0] == xy[1], a))
print(b.count(True))