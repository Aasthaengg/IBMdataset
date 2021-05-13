n = int(input())

def drawKoch(p1, p2, i):
    if i == 0:
        print(*p1)
        return 0
    else:
        s = [p2[0]/3+p1[0]*2/3, p2[1]/3+p1[1]*2/3]
        t = [p2[0]*2/3+p1[0]/3, p2[1]*2/3+p1[1]/3]
        u = [p2[0]/2+p1[0]/2-(p2[1]-p1[1])/(2*(3**0.5)), \
            p2[1]/2+p1[1]/2+(p2[0]-p1[0])/(2*(3**0.5))]
        drawKoch(p1, s, i-1)
        drawKoch(s,  u, i-1)
        drawKoch(u,  t, i-1)
        drawKoch(t, p2, i-1)

p1_start = [0.0, 0.0]
p2_start = [100.0, 0.0]
drawKoch(p1_start, p2_start, n)
print(*p2_start)
