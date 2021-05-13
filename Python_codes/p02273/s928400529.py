from math import cos,sin,radians

n=int(input())

def koch(n):
    if n==0:
        return [[0,0],[100,0]]
    points=koch(n-1)
    new_points=[]
    for i in range(len(points)-1):
        a_x=points[i][0]
        a_y=points[i][1]
        b_x=points[i+1][0]
        b_y=points[i+1][1]
        c_x,c_y=a_x*2/3+b_x/3,a_y*2/3+b_y/3
        d_x,d_y=a_x/3+b_x*2/3,a_y/3+b_y*2/3
        e_x=(d_x-c_x)*cos(radians(60))-(d_y-c_y)*sin(radians(60))+c_x
        e_y=(d_x-c_x)*sin(radians(60))+(d_y-c_y)*cos(radians(60))+c_y
        if [a_x,a_y] not in new_points:
            new_points.append([a_x,a_y])
        new_points.append([c_x,c_y])
        new_points.append([e_x,e_y])
        new_points.append([d_x,d_y])
        if [b_x,b_y] not in new_points:
            new_points.append([b_x,b_y])
    return new_points

for i in koch(n):
    print(*i)
