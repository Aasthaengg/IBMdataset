a, b = (int(input()) for i in [0]*2)
c, d = (int(input()) for i in [0]*2)
u = [a, b]
w = [c, d]
u.sort()
w.sort()
print(u[0]+w[0])