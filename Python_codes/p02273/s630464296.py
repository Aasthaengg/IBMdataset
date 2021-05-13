import math
n = input()
 
p1_x = float(0)
p1_y = float(0)
p2_x = float(100)
p2_y = float(0)
 

def kock(i, n, x1, y1, x2, y2):
    a = [0,0,0,0,0]
    b = [0,0,0,0,0]
    if i < n:
        a[0] = x1
        b[0] = y1
        a[1] = (2*x1+x2)/3.0
        b[1] = (2*y1+y2)/3.0
        a[2] = (x1+2*x2)/3.0
        b[2] = (y1+2*y2)/3.0
        a[3] = (a[2] - a[1])*math.cos(math.pi/3) - (b[2] - b[1])*math.sin(math.pi/3) + a[1]
        b[3] = (b[2] - b[1])*math.cos(math.pi/3) + (a[2] - a[1])*math.sin(math.pi/3) + b[1]
        a[4] = x2
        b[4] = y2
        kock(i+1, n, a[0], b[0], a[1], b[1])
        print a[1], b[1]
        kock(i+1, n, a[1], b[1], a[3], b[3])
        print a[3], b[3]
        kock(i+1, n, a[3], b[3], a[2], b[2])
        print a[2], b[2]
        kock(i+1, n, a[2], b[2], a[4], b[4])

print p1_x, p1_y
kock(0, n, p1_x, p1_y, p2_x, p2_y)
print p2_x, p2_y