import numpy

W, H, N = map(int, input().split())
info = []
for _ in range(N):
    x, y, a = map(int, input().split())
    info.append([x,y,a])

plane = numpy.ones((H, W))

for x, y, a in info:
    if a == 1:
        plane[:, :x] = 0
    elif a == 2:
        plane[:, x:] = 0
    elif a == 3:
        plane[:y, :] = 0
    else:
        plane[y:, :] = 0
    
        
print(int(numpy.sum(plane)))