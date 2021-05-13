def devide2points(p1,p2):
    s=((p1[0]*2+p2[0])/3,(p1[1]*2+p2[1])/3)
    t=((p1[0]+p2[0]*2)/3,(p1[1]+p2[1]*2)/3)
    u=((p1[0]+p2[0])/2-(p2[1]-p1[1])*(3**(1/2))/6,(p1[1]+p2[1])/2+(p2[0]-p1[0])*(3**(1/2))/6)
    return [s,u,t]

def divide(points):
    res = [points[0]]
    for i in range(len(points)-1):
        res = res + devide2points(points[i],points[i+1]) + [points[i+1]]
    return res

n = int(input())
points = [(0.0,0.0),(100.0,0.0)]
for _ in range(n):
    points = divide(points)
for i in points:
    print(i[0],i[1])
